# [DRF] View 작성 방법 - Mixins, Generic CBV, Viewset



## 4. Mixins


기존 APIView에서는 각각의 메소드를 모두 작성해야해서 중복 코드가 길어지는 문제가 있었는데

이를 개선하고자 나온 것이 `Mixins` 이다.

바로 코드를 보자.

```python
# views.py
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins


class User_mixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
	
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail_mixins(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("user/mixins/",views.User_mixins.as_view()),
    path("user/mixins/<int:pk>/",views.UserDetail_mixins.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

```

### 결과

![](https://velog.velcdn.com/images/mechauk418/post/b2219079-1539-42d3-b9e1-52c6f48ed61f/image.jpg)


형태는 비슷하지만 각각의 메소드에서 작성해야할 코드의 분량이 `APIView` 에 비해 상당히 줄었다.

이는 우리가 불러온 `mixins` 에서 코드를 대신 작성해주었기 때문이다.

![](https://velog.velcdn.com/images/mechauk418/post/65220b2f-c739-4eb0-8b61-5c24a75789fb/image.png)

`ListModelMixin`, `CreateModelMixin` 코드를 보면 `APIView` 에서 사용한 것과 유사한 코드가 있는 것을 볼 수 있다.

이것은 `mixins`에서 상속받아 사용하기 때문에 가능한 것이다.
<br>

## 5. Generic CBV
<br>

`mixins` 에서 코드를 더 간결하게 압축하기 위해 사용되는 방식이 `Generic CBV`이다.


```python
# views.py
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins

class User_generic(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail_generic(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("user/generic/",views.User_generic.as_view()),
    path("user/generic/<int:pk>/",views.UserDetail_generic.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

```


마찬가지로 불러온 `generics`에서 미리 정의한 코드를 상속받아서 사용하는 개념이다

https://github.com/encode/django-rest-framework/blob/master/rest_framework/generics.py 

위의 웹페이지에서 `ListCreateAPIView` 를 정의한 코드를 보면

```python
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```


`mixins` 에서 사용한 코드가 그대로 들어가있는 것을 볼 수 있고 우리는 이것을 상속하여 사용하는 것이다.

그리고 마지막으로 가장 압축한 것이 다음에 알아볼 `Viewset` 이다.


## 6. Viewset


```python
# views.py
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets

class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("user/viewset/",views.User_ViewSet.as_view({"post": "create", "get": "list"})),
    path("user/viewset/<int:pk>/",views.User_ViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)


```


코드가 훨씬 간결해진 것을 볼 수 있다.

https://github.com/encode/django-rest-framework/blob/19655edbf782aa1fbdd7f8cd56ff9e0b7786ad3c/rest_framework/viewsets.py

`ModelViewSet`  코드는 위의 링크에서 볼 수 있다.



```python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```

`ModelViewSet` 의 코드를 보면 이렇게 정의하고 있다.

마찬가지로 상속을 받아서 코드를 압축하는 방식이다.

또한, `ViewSet` 에서는 url도 `router`을 사용하여 구현할 수 있다. (위에서 작성한 url과는 다른 방식)

```python
# urls.py
router = DefaultRouter()
router.register('user', views.User_ViewSet)

urlpatterns =[
    path('', include(router.urls))
]
```



참고:https://wisdom-990629.tistory.com/category/%EA%B0%9C%EB%B0%9C/Django%20RESTful%20API