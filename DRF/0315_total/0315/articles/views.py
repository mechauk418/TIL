from django.shortcuts import render
from .models import Article, Comment, Like
from .serializers import ArticleSerializer, CommentSerializer, LikeSerializer 
from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class Article_pagination(PageNumberPagination):
    page_size = 5

class Article_ViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = Article_pagination


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
        )


class Comment_ViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
            article=Article.objects.get(pk=self.kwargs.get("article_pk")),
        )

class LikeCreate(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    serializer_class = LikeSerializer

    def get_queryset(self):
        article = Article.objects.get(pk=self.kwargs.get("article_pk"))
        return Like.objects.filter(article=article)

    def perform_create(self, serializer):
        article = Article.objects.get(pk=self.kwargs.get("article_pk"))
        like = Like.objects.filter(user=self.request.user, article = article)
        if like.exists():
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer.save(
            user=self.request.user,
            article=Article.objects.get(pk=self.kwargs.get("article_pk")),
        )