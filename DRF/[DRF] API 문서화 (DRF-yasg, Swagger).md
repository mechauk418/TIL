

# API 문서화 (DRF-yasg, Swagger)



`Swagger` 은 개발한 Rest API를 편리하게 문서화해주고, 이 문서를 보고 사용자가 API를 호출, 테스트할 수 있게 도와주는 도구이다.



물론 DRF가 엔드포인트를 html로 제공해서 거기서도 테스트를 할 수 있지만, 프로젝트 전체를 한눈에 보고 테스트를 할 수 있는게 `swagger`의 장점이다.



흔히 OpenAPI를 제공하는 사이트에서 볼 수 있는 형식이 `Swagger` 이다.



### 패키지 설치



```bash
pip install drf-yasg
pip install coreapi pyyaml 
```



### 설정



```python

# settings.py

INSTALLED_APPS = [
    'drf_yasg',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 템플릿 주소 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```



```python
# urls.py

from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Todo/", include("Todo.urls")),
    path("accounts/", include("accounts.urls")),
]

### ↓↓↓ 아래 부분 추가

schema_view = get_schema_view(
    openapi.Info(
        title="My Project API",
        default_version="v1",
        description="API documentation for My Project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"), license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```



프로젝트 폴더 하위에 `templates`, `static` 폴더를 추가해준다.



그러고나선 `drf_yasg` 패키지 폴더에서 각각 `templates`, `static` 를 찾아 위에서 만든 폴더에 복사한다.



![](https://velog.velcdn.com/images/mechauk418/post/ac7ac1c1-e12c-4873-80cd-b8358d3271b1/image.jpg)



설정이 끝나면 `http://localhost:8000/docs/` 와 `http://localhost:8000/docs/` 로 접속하여 API를 확인한다.



![](https://velog.velcdn.com/images/mechauk418/post/f8422641-8b24-405f-83da-2157a50ad0cd/image.jpg)



docs에서 확인할 수 있는 API 문서



![](https://velog.velcdn.com/images/mechauk418/post/e3cb92aa-115e-4884-af2a-f6e089e011ef/image.jpg)



swagger에서 확인할 수 있는 API 문서
