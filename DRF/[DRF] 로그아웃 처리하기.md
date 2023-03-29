# [DRF] 로그아웃 처리하기





기존에는 서버측에 로그아웃 요청을 보내는 것이 필요한가? 라는 생각을 했다.

로그인을 할때는 반드시 서버로 요청을 보내서 토큰을 얻어야하지만 로그아웃은 클라이언트에서 토큰만 지워주면 된다고 생각했다.

그런데 refresh token을 http only 쿠키로 설정하니 클라이언트에서 쿠키를 삭제하는 것이 어려워 서버에도 요청을 보내는 것으로 했다.


`dj-rest-auth` 에서 지원하는 logout으로 POST 하는 방식을 사용했다.

그런데

```
Neither cookies or blacklist are enabled,
so the token has not been deleted server side. 
Please make sure the token is deleted client side.
```

라는 오류가 발생했다.

`dj-rest-auth`의 `logoutview` 코드를 보았다.

```Python
        if api_settings.USE_JWT:
            from rest_framework_simplejwt.exceptions import TokenError
            from rest_framework_simplejwt.tokens import RefreshToken

            from .jwt_auth import unset_jwt_cookies
            cookie_name = api_settings.JWT_AUTH_COOKIE

            unset_jwt_cookies(response)

            if 'rest_framework_simplejwt.token_blacklist' in settings.INSTALLED_APPS:
                # add refresh token to blacklist
                try:
                    token = RefreshToken(request.data['refresh'])
                    token.blacklist()
                except KeyError:
                    response.data = {'detail': _('Refresh token was not included in request data.')}
                    response.status_code =status.HTTP_401_UNAUTHORIZED
                except (TokenError, AttributeError, TypeError) as error:
                    if hasattr(error, 'args'):
                        if 'Token is blacklisted' in error.args or 'Token is invalid or expired' in error.args:
                            response.data = {'detail': _(error.args[0])}
                            response.status_code = status.HTTP_401_UNAUTHORIZED
                        else:
                            response.data = {'detail': _('An error has occurred.')}
                            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

                    else:
                        response.data = {'detail': _('An error has occurred.')}
                        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

            elif not cookie_name:
                message = _(
                    'Neither cookies or blacklist are enabled, so the token '
                    'has not been deleted server side. Please make sure the token is deleted client side.',
                )
```



가장 아래 코드에 위에서 발생한 오류 내용이 나온다. `cookie_name` 이 없다고한다.



코드의 중단부를 보면 `cookie_name` 이  `cookie_name = api_settings.JWT_AUTH_COOKIE` 라고 정의된다.



즉, 기존에 `dj-rest-auth`의 setting을 아래와 같이 설정했는데 `JWT_AUTH_COOKIE` 가 없다.

```python
REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_REFRESH_COOKIE' : "refresh_token",
    'JWT_AUTH_COOKIE_USE_CSRF' : True,
    'SESSION_LOGIN' : False
}

```

`logoutview`를 살펴보면 USE_JWT를 사용하면 access token, refresh token 모두 설정을 해야한다.

refresh token만 쿠키로 관리하고 access token은 로컬스토리지에 저장할 것이라 따로 설정을 안했는데 세팅을 바꿀 필요가 있었다.

```python
REST_AUTH = {
    'USE_JWT' : True,
    'JWT_AUTH_COOKIE' : 'access',
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_REFRESH_COOKIE' : "refresh_token",
    'JWT_AUTH_COOKIE_USE_CSRF' : True,
    'SESSION_LOGIN' : False
}

```

access token의 이름인 `JWT_AUTH_COOKIE` 옵션을 추가했다.

쿠키에 access token을 추가했더니 로그아웃 API에 POST요청을 보내면 성공적으로 쿠키가 삭제되는 것을 볼 수 있었다.