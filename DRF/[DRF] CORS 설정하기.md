### Cross-Origin Resource Sharing (CORS)


![](https://velog.velcdn.com/images/mechauk418/post/d53645d9-b8b9-4d12-8384-a0d0a59b46ac/image.jpg)



CORS란 직역하면 교차 출처 리소스 공유로, 간단히 말해서 출처가 다른 리소스를 허용하는 정책이다.

원래 웹페이지는 SOP라는 동일 출처 리소스 공유라는 정책을 사용했는데 시대의 흐름에 따라 출처가 다른 리소스를 가져와서 사용하는 일이 늘어났고

이에 CORS라는 예외를 만든 것이다.

즉, 우리가 볼 수 있는 CORS 에러는 SOP에 예외조항이지만 CORS 규칙마저 지키지 않아서 오류가 발생하는 것이지 CORS 규칙을 잘 지킨다면 좋은 것이라고 볼 수 있다.


CORS에 대한 자세한 설명은 생략하고 Django로 개발하면서 CORS 에러를 접하는 경우는 두번 있었다.

첫번째는 처음으로 프론트엔트에서 백엔드를 호출할때, 두번째는 소셜로그인을 구현할때이다.


### 프론트엔드에서 호출할때

![](https://velog.velcdn.com/images/mechauk418/post/6c360e26-a147-47be-a042-0fedc7cc9084/image.jpg)



에러를 보면 `No 'Access-Control-Allow-Origin' header is present on the requested resource` 라고 나온다.

CORS에러 응답을 보면 헤더에 아무것도 없다. 

django에서는 `django-cors-headers` 라는 라이브러리로 cors 에러를 해결할 수 있다.


https://pypi.org/project/django-cors-headers/ 


### 1) 설치

```git
pip install django-cors-headers
```

### 2) 설정

```python
# settings.py
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",  # 가능한 최상단에 위치할 것
    "django.middleware.common.CommonMiddleware", # 대부분 기본 옵션으로 들어가있다.
    ...,
]

CORS_ALLOW_METHODS = [  # 허용할 옵션
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [ # 허용할 헤더
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_CREDENTIALS = True
```

이후 아래의 세가지 옵션에서 한가지 이상을 설정해준다. (한가지는 필수)

각각 URL, 정규표현식, 전체 허용 or 전체 차단 옵션이다.

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_ALLOW_ALL_ORIGINS: True or False 

```

이렇게 설정해주면 끝난다.

설정 후에 다시 프론트엔드에서 백엔드로 요청을 보내보았다.


![](https://velog.velcdn.com/images/mechauk418/post/9dc594e3-9d07-4f80-aafb-96677ecf6255/image.jpg)


처음과 다르게 요청과 응답도 제대로 이루어졌고 응답에 `Access-Control-Allow-Origin` 헤더가 생긴 것을 볼 수 있다.


이렇게 설정해두면 CORS 에러를 볼일이 거의 없어지는데, 소셜로그인 등 외부 api를 사용할 때 다시 한번 볼 수 있다.

여기에 대한 해결책은 소셜로그인 구현에서 작성하겠다.