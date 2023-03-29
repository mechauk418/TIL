# [DRF] 게시판 조회수 쿠키를 사용한 중복 방지



조회수는 간단하게 구현하려고 하면 게시글 상세보기 요청할때마다 +1 하는 방식으로 간단하게 구현 가능하지만, 이런 방식은 한명이 조회수를 여러번 올리는 행위가 가능하다.

그렇기 때문에 쿠키나 IP 등을 활용하여 중복 조회 방지를 통해 좀 더 유사한 조회수를 구현할 수 있다.

여기서는 쿠키를 활용했다. 


```python
 # articles/views.py

class Article_ViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleSerializer
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

```

Article의 viewset 에서 retrieve를 오버라이딩 해준다.


![](https://velog.velcdn.com/images/mechauk418/post/69c8558e-c82b-4640-8d7a-dec2df909476/image.jpg)


hit라는 쿠키에 내가 조회한 게시글의 pk가 담기는 것을 확인할 수 있다.


참고 : 
[Django-mysite만들기9 게시판 조회수 중복 증가 쿠키 처리
](https://jungeunlee95.github.io/django/2019/06/25/mysite%EB%A7%8C%EB%93%A4%EA%B8%B0-9-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EC%A1%B0%ED%9A%8C%EC%88%98-%EC%A4%91%EB%B3%B5-%EC%A6%9D%EA%B0%80-%EC%BF%A0%ED%82%A4-%EC%B2%98%EB%A6%AC/)

[DRF 게시글 생성 및 조회수 중복 방지(쿠키 설정)
](https://moondol-ai.tistory.com/216)