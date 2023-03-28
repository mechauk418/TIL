# [DRF] dj-rest-auth JWT 세팅 관련 변경된 점 + http only 쿠키 설정법



12월에 `dj-rest-auth` 로 프로젝트를 진행했었는데 불과 3개월이 안되서 기존 코드가 작동하지 않았다.

프로젝트 당시에는 2.2.5버전을 사용했는데 최신 버전은 3.0.0이였다.

변경된 점은 아래와 같다.

```python
#settings.py

// 2.2.5버전
REST_USE_JWT = True -> 

// 3.0.0버전
REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_HTTPONLY': False,
}

```

`settings.py` 에서 `dj-rest-auth` 관련  설정이 모두 하나로 묶였다.

그런데 이렇게만 설정해주면 로그인 시 refresh token이 빈칸으로 나오는 것을 볼 수 있다.

`'JWT_AUTH_HTTPONLY': True`

이 설정이 기본적으로 `True`로 설정되어있기 때문인데, 이것을 `False`로 바꿔주면 평소처럼 access, refresh token 모두 응답받을 수 있다.

그런데 refresh token을 보안상의 이유로 http only 쿠키로 설정해야할 필요가 있다.

아래와 같이 설정하였다.


```python

REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_REFRESH_COOKIE' : "refresh_token",
    'JWT_AUTH_COOKIE_USE_CSRF' : True,
    'SESSION_LOGIN' : False
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    )
}

```

`JWT_AUTH_HTTPONLY` : 쿠키를 http only로 할건지 여부 (기본 True)


`JWT_AUTH_REFRESH_COOKIE` : refresh token을 담을 쿠키 이름 (기본 None)

`JWT_AUTH_COOKIE_USE_CSRF` : JWT 쿠키 csrf 검사
`SESSION_LOGIN`: 세션 로그인 기능 (기본 True)

세션 로그인을 `False` 로 하지 않으면  `sessionid`가 쿠키로 남기 때문에 지워주었다.

(`DEFAULT_AUTHENTICATION_CLASSES` 에서 `        "rest_framework.authentication.SessionAuthentication",
` 지우면 API 엔드포인트에서 로그인이 안되니 주의하자)

![](https://velog.velcdn.com/images/mechauk418/post/4847fa36-8193-4b31-9f5b-1b86a66bc5e0/image.jpg)

http only 에 체크되어있다.

![](https://velog.velcdn.com/images/mechauk418/post/c8bf490a-6b20-48db-8ee6-ce51b77dc8f2/image.jpg)

refresh token은 쿠키로 전달되어 response에서 빈칸으로 처리된다.



정말 많이 헤맸는데 구글 로그인때와 마찬가지로 패키지의 버전 문제였다.