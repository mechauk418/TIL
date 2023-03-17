# [DRF] DRF 계정 관리하기





DRF 4종류의 View 를 알아보기전에 앞서 DRF에서의 계정 관리부터 알아보겠다.

왜냐하면 어떤 프로젝트던 계정 시스템이 먼저 구축되어야 만들기 편하기 때문이다.


DRF에서는 계정 관리를 위해 `dj_rest_auth` 와 `django-allauth`  이 두개의 라이브러리를 사용한다.


### dj_rest_auth

https://dj-rest-auth.readthedocs.io/

로그인, 로그아웃, 사용자 등록, 비밀번호 등록, 소셜로그인 등을 지원해주는 라이브러리이다.


### 1. 설치하기

```bash
pip install dj-rest-auth

```

```python
# settings.py
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'
)
```

```python
# url.py
urlpatterns = [
    ...,
    path("accounts/", include("dj_rest_auth.urls")),
]
```


dj_rest_auth 설치 후에 기본적인 세팅을 해준다.



### 2. User 모델 입력

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    pass
```

User 모델을 설정해준다.

![](https://velog.velcdn.com/images/mechauk418/post/d337821f-8b93-484f-827f-7f56b843ea28/image.jpg)

마이그레이션을 하고 서버를 켜서 설정한 URL로 들어가보면 dj_rest_auth에서 기본적으로 지원하는 api를 볼 수 있다.

그러나 잘 보면 유저 등록을 찾아볼 수 없는데, 유저 등록은 `django-allauth` 으로 해야한다.

```bash
pip install django-allauth

```

```python
# settings.py
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth',
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
)
SITE_ID = 1
```

```python
# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("dj_rest_auth.urls")),
    path('accounts/registration/', include('dj_rest_auth.registration.urls'))
]

```

마찬가지로 설치 후 기본적인 세팅을 해준다.

![](https://velog.velcdn.com/images/mechauk418/post/cacf958f-ac88-46bc-b3b9-77e0d83988c2/image.jpg)

그 후 유저 등록 URL로 들어가면 유저를 등록(회원가입)시킬 수 있다.

여기까지만 해도 기본적인 회원 관리를 쉽게 적용시킬 수 있다.

다음 포스팅에서는 JWT 방식을 통한 로그인을 알아보겠다.