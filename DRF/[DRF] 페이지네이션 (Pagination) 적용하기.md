# [DRF] 페이지네이션 (Pagination) 적용하기



![](https://velog.velcdn.com/images/mechauk418/post/cddb65a0-7009-4fbe-a982-9c9c061b46fd/image.jpg)

게시판 구현에서 페이지네이션은 필수이다. (무한 스크롤도 페이지네이션을 기반으로 한다)

페이지네이션 처리전에는 그림처럼 모든 목록이 나온다.

DRF는 페이지네이션을 지원해서 간단하게 설정할 수 있다.

```python
# settings.py

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5, # 페이지 당 데이터 갯수
}

```

![](https://velog.velcdn.com/images/mechauk418/post/129ed564-5946-4c79-ae20-4dd245e35783/image.jpg)

페이지네이션 후에 api를 확인하면 데이터가 5개씩 잘려있고 URL에서 ?page=N 이라는 파라미터를 확인할 수 있다.

만약 특정한 API에만 페이지네이션이 필요하다면 views.py에서 설정할 수 있다.


```python
 
 # articles/views.py
 
 class Article_pagination(PageNumberPagination):
    page_size = 2

class Article_ViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = Article_pagination


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user,
        )

```

![](https://velog.velcdn.com/images/mechauk418/post/4bd8f98f-8ccc-4d20-8cfa-47247bfca132/image.jpg)

페이지 사이즈가 전역은 5지만 articles는 view에서 따로 설정했기때문에 페이지 사이즈가 2로 나온다.