# Authentication , Permissions





DRF는 즉시 사용가능한 몇가지 인증체계 및 인증체계 커스텀을 제공한다.



인증된 클래스가 없으면 `request.user`는 `django.contrib` 인스턴스로 설정된다.



인증은 요청을 허용하거나 허용하지 않거나 둘 중 하나를 가리는 것이다.



즉, 시스템에 등록된 사람인지를 판별하는 것이 `Authentication ` 이라면, 이 사람의 요청이 정당한지를 판단하는 것은 `Permissions` 이다.







### 기본 인증체계

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

```



프로젝트 전역에 대한 기본 인증을 설정할 수 있다.



### 개별 인증체계



```python
# views.py
from rest_framework.authentication import SessionAuthentication 

class testViewSet(ModelViewSet):
    
    authentication_classes = (SessionAuthentication, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

```



이러한 방법으로 각각의 views 에 대한 인증 체계를 설정할 수 있다.



### 기본 권한체계



```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    ),

}
```



프로젝트 전역에 대한 기본 권한을 설정할 수 있다.



### 개별 권한체계



```python
# views.py

class testViewSet(ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # 해당 뷰셋 전체에 개별인증체계를 적용
   	permission_classes = [permissions.AllowAny, ]

    
    # 해당 뷰셋에서 각각의 actions 행위에 개별 인증체계를 적용시킨다.
    # 즉 list, create, update 각각의 행위에 다른 인증체계를 적용시킬 수 있다.
    def get_permissions(self):
    """
    Instantiates and returns the list of permissions that this view requires.
    """
    if self.action == 'list':
        permission_classes = [IsAuthenticated]
    else:
        permission_classes = [IsAdminUser]
    return [permission() for permission in permission_classes]
```

