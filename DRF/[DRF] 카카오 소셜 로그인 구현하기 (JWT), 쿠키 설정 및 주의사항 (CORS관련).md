# [DRF] 카카오 소셜 로그인 구현하기 (JWT), 쿠키 설정 및 주의사항 (CORS관련)

<br>

### 시작하기

DRF에서 모든 인증과정은 아래 3개의 패키지를 기반으로 하므로 설치해주자.

```python
pip install django-allauth
pip install dj-rest-auth
pip install djangorestframework-simplejwt
```

이 포스팅은 아래의 블로그 글을 기반으로 했다.

[Django-Rest-Framework(DRF)로 소셜 로그인 API 구현해보기(Google, KaKao, Github)](https://medium.com/chanjongs-programming-diary/django-rest-framework%EB%A1%9C-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-api-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EA%B8%B0-google-kakao-github-2ccc4d49a781)

DRF로 소셜로그인을 구현하려는 사람들은 한번쯤은 찾아봤을 것이다.

그런데 직접 해보면서 코드를 조금 바꿔야할 부분이 있어서 수정해서 적용시켜보았다.


```python
# urls.py

from django.urls import path, include
from .views import kakao_callback, KakaoLogin # Import the above views

urlpatterns = [
    path("kakao/callback/", kakao_callback, name="kakao_callback"),
    path(
        "kakao/login/finish/", KakaoLogin.as_view(), name="kakao_login_todjango"
    ),
]
```

```python

# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'accounts',
    "allauth",
    "allauth.account",
    'allauth.socialaccount',
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    'rest_framework_simplejwt',

]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.CustomUserRegisterSerializer"
}  # 유저 회원가입



REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_COOKIE' : 'access',
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_REFRESH_COOKIE' : "refresh_token",
    'JWT_AUTH_SAMESITE': 'Lax',
    'JWT_AUTH_COOKIE_USE_CSRF' : False,
    'SESSION_LOGIN' : False
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
}

```





```python
# views.py

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

BASE_URL = "http://localhost:8000/"

KAKAO_CALLBACK_URI = "http://localhost:8080/login"  # 프론트 로그인 URI 입력

@api_view(["GET"])
@permission_classes([AllowAny])
def kakao_callback(request):
    rest_api_key = '카카오 REST API 키 입력'  # 카카오 앱키, 추후 시크릿 처리
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
        cookie_max_age = 3600 * 24 * 14 # 14 days
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

```


상당히 복잡해보이는데 한줄한줄 뜯어보면 어렵지 않다.

아래는 카카오 API에서 제공하는 카카오 소셜로그인 과정이다.

![](https://velog.velcdn.com/images/mechauk418/post/4f0b8c9c-91b0-4368-b65f-2492ecfe50f3/image.jpg)


### 1. 카카오 로그인 요청

프론트에서 카카오 소셜로그인을 하겠다고 카카오 서버로 요청한다.

### 2. 인가 코드 받기 요청

![](https://velog.velcdn.com/images/mechauk418/post/e0cdb7c8-de71-4e53-9462-58a0d42b1d8a/image.jpg)

프론트에서 앱키, redirect_URI를 받아서 카카오 서버로 코드 요청을 보낸다.

### 3. 인증 및 동의 요청 ~ 로그인 및 동의

흔히 보는 카카오톡 로그인 및 인증 / 동의요청 창이 뜬다.

### 4. 인가 코드 발급

인증이 완료되면 코드를 발급한다.

이 코드는 반드시 프론트엔드에서 쿼리스트링으로 받아야한다.

![](https://velog.velcdn.com/images/mechauk418/post/1c6f7d43-bd83-461a-8e24-570480882ed3/image.jpg)

url에 코드가 담겨서 본래 창으로 돌아왔다.

### 5. 인가 코드로 토큰 발급 요청

인가 코드를 백엔드로 전달하여 카카오로 부터 토큰을 발급받는다.

여기서 말하는 토큰은 JWT가 아닌 카카오의 토큰이다.

위의 콜백함수에서 아래가 이 부분에 해당한다.

```python
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}"
    )
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
```

### 6. 발급받은 토큰으로 서비스 로그인 처리

발급받은 토큰으로 우리 서비스의 JWT 토큰을 발급받고 로그인 처리해준다.

여기서 아래의 카카오 뷰가 쓰인다.

```python

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8080/login" 

```

urls.py 에서 설정한 엔드포인트로 가보면 카카오 로그인뷰는 아래와 같이 access token(카카오에서 발급한)과 code를 받아서 서비스에서 사용하는 JWT 토큰을 반환해주는 뷰라는 것을 알 수 있다.

![](https://velog.velcdn.com/images/mechauk418/post/0ca2b015-e59e-4f29-af16-fc89fc1001c0/image.jpg)

![](https://velog.velcdn.com/images/mechauk418/post/f5dd2b81-e610-4d4d-82a6-1af9fe72b5c6/image.jpg)

```python

	data = {"access_token": access_token, "code": code}
    accept = requests.post(f"{BASE_URL}accounts/kakao/login/finish/", data=data)
    accept_status = accept.status_code
    	if accept_status != 200:
			return JsonResponse({"err_msg": "failed to signin"}, status=accept_status)
        accept_json = accept.json()

```

그래서 아래의 뷰에 요청을 날리면 응답을 받을 수 있다.

일반적으로는 access token과 refresh token 모두 응답해주기 때문에 이 토큰을 프론트로 전달해주면 끝이지만 refresh token을 http only 쿠키로 구현하는 것을 목적으로 하고 있기 때문에 쿠키를 설정해줘야한다.

### 7. refresh token 파싱


```python
        # refresh_token을 headers 문자열에서 추출함
        refresh_token = accept.headers['Set-Cookie']
        refresh_token = refresh_token.replace('=',';').replace(',',';').split(';')
        token_index = refresh_token.index(' refresh_token')
        cookie_max_age = 3600 * 24 * 14 # 14 days
        refresh_token = refresh_token[token_index+1]
        accept_json.pop("user", None)
        response_cookie = JsonResponse(accept_json)
        response_cookie.set_cookie('refresh_token', refresh_token, max_age=cookie_max_age, httponly=True, samesite='Lax')
        return response_cookie

```

`accept.headers` 를 print해보면 아래와 같은 헤더 정보가 보인다.

![](https://velog.velcdn.com/images/mechauk418/post/f2f5e750-66ff-44bb-a768-ee4c540469f3/image.jpg)

여기서 `Set-Cookie` 에 있는 refresh token 값만 파싱해서 `set_cookie` 메소드를 통해 응답에 쿠키를 담았다.

### 8. django admin 설정

django admin에서 아래와 같이 소셜 로그인 관련 설정을 해준다.

![](https://velog.velcdn.com/images/mechauk418/post/7340e6ba-a68e-447b-af43-f62b1f791cc4/image.jpg)

![](https://velog.velcdn.com/images/mechauk418/post/2dcf7f39-1709-4b9c-a11e-55c376e3c268/image.jpg)



### 9. 결과


![](https://velog.velcdn.com/images/mechauk418/post/5df9ef7a-2b26-498b-a310-1304665849be/image.webp)

로그인이 성공하면 refresh token이 쿠키로 생성되는 것을 볼 수 있다.


### 주의사항

참조 블로그 코드에서 주의할 것이 있다.

바로 CORS이다.

일반적으로 API 서비스는 CORS를 허용하지 않는다.

```python

def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )

```

원문의 해당 view는 프론트에서 진행한 1~4번 과정을 나타내는 코드이다.

그런데 이 코드를 사용하면 프론트에서 리다이렉트되어 API를 바로 호출하는 것이 되어 CORS 에러에 부딪힌다.

CORS 에러를 피하기 위해 프론트에서 해당 과정을 구현하는 것이다.