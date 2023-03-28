# [DRF] 권한 (Permissions)



## 권한 설정 방법 (전역)



```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', ## <<-- 여기에 넣는다
    ]
}
```



`settins.py` 에 해당 설정을 하면 프로젝트 전역에 대한 권한 정책이 설정된다.

만약 해당 설정을 지정하지 않으면 기본적으로 `   rest_framework.permissions.AllowAny` (누구나 허용)이다.



## 권한 설정 방법 (부분)



```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
```



```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)
```



`    permission_classes = [IsAuthenticated]`

`@permission_classes([IsAuthenticated])`

CBV, FBV 방식에 따라 다음과 같이 부분에 해당하는 권한을 설정해줄 수 있다.







## 권한 종류



- AllowAny - 무제한 액세스를 허용한다. (기본값)
- IsAuthenticated - 인증된 유저의 요청에만 액세스를 허용한다 (로그인 유무)
- IsAdminUser - `is_staff = True` 인 유저의 요청에만 액세스를 허용한다. 
- IsAuthenticatedorReadOnly - 인증된 유저가 아닌 경우에는 `GET`, `HEAD`, `OPTIONS` 요청만 허용한다.
- DjangoModelPermissions - 유저가 인증되고, 관련 모델에 권한이 있는 경우에만 액세스를 허용한다.
- DjangoModelPermissionsorAnonReadOnly - `DjangoModelPermissions ` 과 유사하나 유저가 인증되지 않은 경우는 `GET`, `HEAD`, `OPTIONS` 요청만 허용한다.
- DjangoObjectPermissions - 모델에 대해 객체 별 권한을 설정하여 유저가 인증되고, 관련 모델과 객체에 권한이 있는 경우에만 액세스를 허용한다.
- Custom Permissions - 개발자가 권한 조건을 커스텀하는 경우다.





## 권한 커스텀



```python
# articles/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): # Basepermission을 상속받음
    def has_object_permission(self, request, view, obj):
        # 읽기 권한 요청이 들어오면 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 요청자(request.user)가 객체(Article)의 user와 동일한지 확인
        return obj.user == request.user

    
# views.py

class Article_ViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = Article_pagination


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
        )
```



- 권한 커스텀이 필요한 경우 `permissions.py` 에서 새로운 권한을 정의하여 `views.py`에서 불러오는 방식으로 할 수 있다.