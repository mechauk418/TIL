# [DRF] DRF(Django REST Framework) 시작하기



![](https://velog.velcdn.com/images/mechauk418/post/403ad542-6628-4783-905c-0f1062dae19f/image.png)


DRF란 Django에서 지원하는 RESTful API 라이브러리를 말한다.

REST란 REpresentational State Transfer 의 약자로 자원의 이름으로 서버와 클라이언트가 통신하는 방법을 말한다.

RESTful API가 급부상한 가장 큰 원인은 웹 브라우저 이외에도 모바일 등 다양한 멀티플랫폼 사이의 통신이 필요해졌기 때문에 효율적인 통신을 위해 관심을 끌게 되었다.

설치를 시작하기에 앞서 자세한 설명은 아래의 공식 홈페이지에서 참고하길 바란다.

https://www.django-rest-framework.org/

<br>

<br>

### pip 설치

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

<br>

<br>

### settings.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

<br>

<br>

### urls.py

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

<br>

<br>




여기까지가 기본 설정이고 다음부터는 view의 5가지 방식을 알아보도록 하겠다.