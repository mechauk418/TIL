# [DRF] View 작성 방법 - @api_view, APIView



Django에서 view를 작성하는 패턴은 두가지가 있다.

1. **CBV (Class Based View)**

2. **FBV (Function Based View)**

클래스와 함수를 사용하여 구현하는 것인데 이 패턴은 DRF에서도 그대로 적용된다.

그러나 어떤 것이 더 좋은 방법인가에 대해서는 확실하지 않은 것 같다.

FBV가 더 자유도가 높은 대신 CBV가 간단한 구현에 한해서는 더 편리했다.

또한, FBV는 기존의 Django 개발과 큰 차이가 없었는데 CBV는 DRF에 대한 지식을 필요로 한다.

결국 두 방식 모두 채택했다. 간단한 구현은 CBV로 하고 복잡한 것은 FBV로 구현하는 식이였다. 


앞선 포스팅에서 view가 5가지 방식이 있다고 했는데 아래와 같은 방식이 있다.

1. `@api_view` (FBV)
2. `APIView` (CBV)
3. `Mixins` (CBV)
4. `Generic CBV` (CBV)
5. `ViewSet` (CBV)

1번을 제외하고는 모두 CBV방식이며 CBV내에서도 아래로 갈수록 코드가 간결해진다.

그러나 상속을 활용하여 코드를 축약한 것이므로 해당 방식에 대한 이해가 필요하다.


### 1. @api_view (FBV)

```python
# views.py
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsOwnerOrReadOnly])
def my_page(request, user_pk):
    if request.method == "GET":

        user_info = get_object_or_404(User, pk=user_pk)
        comment = Comment.objects.filter(user=user_info)
        serializers = UserInfo(user_info)
        # user_article = Article.objects.filter(user=request.user)
        user_comment = Comment.objects.filter(user=user_info)
        user_recomment = ReComment.objects.filter(user=user_info)
        # user_profile = Profiles.objects.get(user=user_info)
        user_score = Score.objects.get(user=user_info)
        user_grass = Grass.objects.get(user=user_info)
        # user_pick = Pick.objects.filter(user=request.user)
        user_like_comment = Like.objects.filter(user=user_info)
        comment = []
        likecomment = []
        for c in user_like_comment:
            likecomment.append(c.comment.pk)
        for c in user_comment:

            comment.append(
                {
                    "content": c.content,
                    "article_pk": c.article.pk,
                    "created_at": c.created_at.strftime("%Y-%m-%d %H:%M"),
                    "article": c.article.title,
                    "A": c.article.A,
                    "B": c.article.B,
                }
            )
        for r in user_recomment:
            comment.append(
                {
                    "content": r.content,
                    "article_pk": r.article.pk,
                    "created_at": r.created_at.strftime("%Y-%m-%d %H:%M"),
                    "parent": r.parent.pk,
                    "article": r.parent.article.title,
                    "A": r.parent.article.A,
                    "B": r.parent.article.B,
                }
            )
        all_data = {
            "user_pk": user_pk,
            "comment": comment,
            "likecomment": likecomment,
            "userinfo": serializers.data,
            # "grade": user_profile.grade,
            "all_score": user_score.total,
            "today_score": user_score.today,
            #  user_grass
            "year": user_grass.year,
            "month": user_grass.month,
            "monthrange": user_grass.monthrange,
            "daylist": user_grass.daylist,
            "consecutive": user_grass.consecutive,
        }
        return Response(all_data)

    # 유저정보 수정 put메서드 사용 (raise_exception=True<- (commit=True)와 같은 역활
    elif request.method == "PUT":
        if request.user.is_authenticated:
            user_pk = request.data["user_pk"]
            badge_pk = request.data["badge_pk"]
            user = User.objects.get(pk=user_pk)
            badge = get_object_or_404(Badge, pk=badge_pk)
            profile = Profiles.objects.get(user=user)
            profile.badge = badge
            profile.save()
            badgeSerializer = BadgeDetailSerializer(badge)
            return Response(badgeSerializer.data, status=200)
    elif request.method == "PATCH":
        if request.user.is_authenticated:
            nickname = request.data["nickname"]
            user = User.objects.get(pk=user_pk)
            user.nickname = nickname
            user.save()
            userSerializer = CustomUserDetailsSerializer(user)
            return Response(userSerializer.data, status=200)
    elif request.method == "DELETE":
        if request.user.is_authenticated:
            user = User.objects.get(pk=user_pk)
            if user != request.user:
                return Response({"result": "본인만 삭제 할 수 있습니다."})
            user.delete()
            return Response({"result": "user delete"})
```

```python
# urls.py
urlpatterns = [
    path("<int:user_pk>/my_page/", views.my_page, name="my_page"),
]
```

유저 정보를 가져오는 코드를 예시로 작성하였다.

Django MTV로 웹페이지를 만드는 것처럼 함수를 작성하고 메소드를 나누어 코드를 작성한다
그리고 함수 위에 `@api_view` 라는 데코레이터를 작성해준다.



### 2. APIView (CBV)

API View는 HTTP의 각각의 메소드를 정의해서 하나씩 붙여나가는 방식이다.

즉, 본인이 작성한 메소드만 사용가능해서 개별적인 커스텀이 가능하다는 장점이 있지만 반대로 모든 메소드를 직접 정의해줘야 하는 번거로움이 있기도 하다.


```python
# views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class User_APIView(APIView): # 리스트

    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users,many = True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data)
        return Response(serializer.errors)
        
class UserDetail_APIView(APIView): # 디테일
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("user/apiview/",views.User_APIView.as_view()),
    path("user/apiview/<int:pk>/",views.UserDetail_APIView.as_view()),
]
```

### 결과

![](https://velog.velcdn.com/images/mechauk418/post/e8138e7e-6186-4fb7-8097-1f9a490fbb8a/image.jpg)


작성했던 GET, POST 만 허용하는 것을 볼 수 있다.