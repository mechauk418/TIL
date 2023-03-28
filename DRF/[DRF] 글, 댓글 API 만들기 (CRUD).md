# [DRF] 글, 댓글 API 만들기 (CRUD)



`accounts`  과 비슷하게 model, serializers, views 를 구성해주면 된다.

### models.py

```python
# articles/models.py

from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    content = models.TextField()

    def __str__(self):
        return self.content

```

모델은 django와 큰 차이는 없다

### serializers.py


```python
# articles/serializers.py

from rest_framework import serializers
from articles.models import *


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    article = serializers.ReadOnlyField(source="article.pk")

    class Meta:
        model = Comment
        fields = [
            "pk",
            "article",
            "user",
            "userpk",
            "content",
            "created_at",
        ]


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            "pk",
            "title",
            "user",
            "userpk",
            "comments",
            "content"
        ]
```

serializers에는 모델의 필드를 용도에 따라 다르게 작성해야함

1. ReadOnlyField

serializers에서 정의하는 읽기만 하는 필드는 ReadOnlyField로 작성한다

2. write_only
```python
password = serializers.CharField(write_only = True)
```
비밀번호같은 쓰기만 는 필드는 write_only로 작성한다.

3. 둘 다 하는 필드

읽기 쓰기 모두 하는 필드는 모델에서 정의만 해주면 된다.

4. read_only_fields 

model에서 정의하는 읽기만 하는 필드는 read_only_fields로 작성한다.
```python
class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            "pk",
            "title",
            "user",
            "userpk",
            "comments",
            "content"
        ]
        read_only_fields = ('id',)

```

### views.py

```python
# articels/views.py
from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
        )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
            article=Article.objects.get(pk=self.kwargs.get("article_pk")),
        )
```

`perform_create`은 오버라이딩을 할수있게해준다.

django에서 request를 가로채서 유저 필드를 request.user로 채워주던 것과 비슷한 방식으로 동작한다.


### urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'articles'

router = DefaultRouter()
router.register('', views.ArticleViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path("<int:article_pk>/comment/", views.CommentViewSet.as_view({"post": "create", "get": "list"})),
]

```

`as_view` 뒤에 오는 부분은 viewset의 응답을 제한할 수 있다. (현재는 post, get만 가능)



### 결과

![](https://velog.velcdn.com/images/mechauk418/post/915cd6e8-4fca-4e65-8f55-e006a7e8b9c6/image.jpg)



글, 댓글 API가 생성되었다.