from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
# Create your views here.
from django.conf import settings
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from rest_framework.response import Response
from dj_rest_auth.registration.views import SocialLoginView
import requests
from allauth.socialaccount.models import SocialAccount
from rest_framework.permissions import AllowAny
from allauth.account.adapter import get_adapter

class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


BASE_URL = "http://localhost:8000/"


KAKAO_CALLBACK_URI = "http://localhost:8080/login"  # 프론트 로그인 URI 입력


@api_view(["GET"])
@permission_classes([AllowAny])
def kakao_callback(request):
    rest_api_key = '17927c83c8f77eef6c83ef6dd7ff221c'  # 카카오 앱키, 추후 시크릿 처리
    code = request.GET.get("code")
    print(code)
    redirect_uri = KAKAO_CALLBACK_URI
    """
    Access Token Request
    """
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}"
    )
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    print(access_token)
    """
    Email Request
    """
    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    profile_json = profile_request.json()
    error = profile_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    kakao_account = profile_json.get("kakao_account")
    """
    kakao_account에서 이메일 외에
    카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
    print(kakao_account) 참고
    """
    email = kakao_account.get("email")
    """
    Signup or Signin Request
    """

    cookie_max_age = 3600 * 24 * 14 # 14 days
    
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse(
                {"err_msg": "email exists but not social user"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if social_user.provider != "kakao":
            return JsonResponse(
                {"err_msg": "no matching social type"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # 기존에 kakao로 가입된 유저
        data = {"access_token": access_token, "code": code}
        accept = requests.post(f"{BASE_URL}accounts/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({"err_msg": "failed to signin"}, status=accept_status)
        accept_json = accept.json()
        # refresh_token을 headers 문자열에서 추출함
        refresh_token = accept.headers['Set-Cookie']
        refresh_token = refresh_token.replace('=',';').replace(',',';').split(';')
        token_index = refresh_token.index(' refresh_token')
        refresh_token = refresh_token[token_index+1]

        accept_json.pop("user", None)
        response_cookie = JsonResponse(accept_json)
        response_cookie.set_cookie('refresh_token', refresh_token, max_age=cookie_max_age, httponly=True, samesite='Lax')
        return response_cookie
    
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {"access_token": access_token, "code": code}
        accept = requests.post(f"{BASE_URL}accounts/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({"err_msg": "failed to signup"}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴

        accept_json = accept.json()
        # refresh_token을 headers 문자열에서 추출함
        refresh_token = accept.headers['Set-Cookie']
        refresh_token = refresh_token.replace('=',';').replace(',',';').split(';')
        token_index = refresh_token.index(' refresh_token')
        refresh_token = refresh_token[token_index+1]

        accept_json.pop("user", None)
        response_cookie = JsonResponse(accept_json)
        response_cookie.set_cookie('refresh_token', refresh_token, max_age=cookie_max_age, httponly=True, samesite='Lax')
        return response_cookie


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8080/login" 

    
    
    
    def process_login(self):

        get_adapter(self.request).login(self.request, self.user)



