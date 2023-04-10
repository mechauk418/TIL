from django.shortcuts import render, get_object_or_404
from .models import Article, Comment, Like
from .serializers import ArticleSerializer, CommentSerializer, LikeSerializer, PostSerializer
from rest_framework import viewsets, status, generics, mixins
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
import datetime
from django.utils import timezone
from rest_framework.views import APIView
# Create your views here.
class Article_pagination(PageNumberPagination):
    page_size = 5

class Article_ViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = Article_pagination

    def list(self, request):
        qs = self.get_queryset()
        page = self.paginate_queryset(qs)
        

        if page is not None:
            serializer = self.get_paginated_response(self.get_serializer(page, many=True).data)
        else:
            serializer = self.get_serializer(page, many=True)

        return  Response(serializer.data, status=status.HTTP_200_OK)


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
        )

    def retrieve(self, request, pk=None):

        instance = get_object_or_404(self.get_queryset(), pk=pk)
        # 당일날 밤 12시에 쿠키 초기화
        tomorrow = datetime.datetime.replace(timezone.datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")
        
        # response를 미리 받고 쿠키를 만들어야 한다
        serializer = self.get_serializer(instance)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        # 쿠키 읽기 & 생성
        if request.COOKIES.get('hit') is not None: # 쿠키에 hit 값이 이미 있을 경우
            cookies = request.COOKIES.get('hit')
            cookies_list = cookies.split('|') # '|'는 다르게 설정 가능 ex) '.'
            if str(pk) not in cookies_list:
                response.set_cookie('hit', cookies+f'|{pk}', expires=expires) # 쿠키 생성
                instance.hits += 1
                instance.save()
                    
        else: # 쿠키에 hit 값이 없을 경우(즉 현재 보는 게시글이 첫 게시글임)
            response.set_cookie('hit', pk, expires=expires)
            instance.hits += 1
            instance.save()

        # hits가 추가되면 해당 instance를 serializer에 표시
        serializer = self.get_serializer(instance)

        return response


class Comment_ViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            article=Article.objects.get(pk=self.kwargs.get("pk")),
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

