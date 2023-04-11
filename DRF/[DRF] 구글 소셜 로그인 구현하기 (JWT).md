# [DRF] 구글 소셜 로그인 구현하기 (JWT)



[[DRF] 카카오 소셜 로그인 구현하기 (JWT), 쿠키 설정 및 주의사항 (CORS관련)](https://velog.io/@mechauk418/DRF-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-JWT-%EC%BF%A0%ED%82%A4-%EC%84%A4%EC%A0%95-%EB%B0%8F-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD-CORS%EA%B4%80%EB%A0%A8)

전체적인 코드는 카카오 로그인에서 사용한 것과 비슷하다.

```python
#views.py

GOOGLE_CALLBACK_URI = "http://localhost:8080/login"  # 프론트 로그인 URI 입력


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def google_callback(request):
    client_id = '구글 클라이언트 ID'
    client_secret = '구글 시크릿 키'
    code = request.GET.get("code")
    print(code)
    """
    Access Token Request
    """
    state = 'gklawfmasdf' # 난수
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}"
    )
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    """
    Email Request
    """
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}"
    )
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse(
            {"err_msg": "failed to get email"}, status=status.HTTP_400_BAD_REQUEST
        )
    email_req_json = email_req.json()
    email = email_req_json.get("email")
    """
    Signup or Signin Request
    """

    cookie_max_age = 3600 * 24 * 14 # 14 days

    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse(
                {"err_msg": "email exists but not social user"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if social_user.provider != "google":
            return JsonResponse(
                {"err_msg": "no matching social type"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # 기존에 Google로 가입된 유저
        data = {"access_token": access_token, "code": code}
        accept = requests.post(f"{BASE_URL}accounts/google/login/finish/", data=data)
        accept_status = accept.status_code
        print(accept.headers)
        if accept_status != 200:
            return JsonResponse({"err_msg": "failed to signin"}, status=accept_status)
        accept_json = accept.json()
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
        accept = requests.post(f"{BASE_URL}accounts/google/login/finish/", data=data)
        print(accept.headers)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({"err_msg": "failed to signup"}, status=accept_status)
        accept_json = accept.json()
        refresh_token = accept.headers['Set-Cookie']
        refresh_token = refresh_token.replace('=',';').replace(',',';').split(';')
        token_index = refresh_token.index(' refresh_token')
        refresh_token = refresh_token[token_index+1]

        accept_json.pop("user", None)
        response_cookie = JsonResponse(accept_json)
        response_cookie.set_cookie('refresh_token', refresh_token, max_age=cookie_max_age, httponly=True, samesite='Lax')
        return response_cookie


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client

```

카카오와 아주 조금 다른게 있다면 `state` 라는 랜덤한 문자열이 필요하다.

이 `state`는 csrf 공격을 방지하기 위한 토큰같은 개념이다.

구글 로그인에 필요한 키는 아래의 링크에서 생성할 수 있다.

https://console.cloud.google.com/getting-started?hl=ko


![](https://velog.velcdn.com/images/mechauk418/post/505cf817-bdff-4638-bc73-498c7ec21834/image.jpg)
![](https://velog.velcdn.com/images/mechauk418/post/51d03ad9-ca83-4588-88a9-a0c4b29ab18e/image.jpg)

클라이언트 ID와 보안 비밀번호를 받고, 리디렉션 URI에 콜백URI를 입력해주면 된다.