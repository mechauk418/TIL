# [DRF] 다중 이미지 업로드하기



Serializer을 중첩시키는 방법으로 다중 이미지 업로드를 구현할 수 있다.

### 코드

```python
# models.py
class PostImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", null=True, blank=True)
# serializers.py

class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = [
            'image',
            ]

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    comments = CommentSerializer(many=True, read_only=True)
    like_article = LikeSerializer(many=True, read_only=True)
    
	#게시글에 등록된 이미지들 가지고 오기
    def get_images(self, obj):
        image = obj.image.all() 
        return PostImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Article
        fields = [
            'pk',
            "user",
            "userpk",
            "title",
            "content",
            "comments",
            "like_article",
            'created_at',
            'hits',
            'images',
        ]

    def create(self, validated_data):
        instance = Article.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(article=instance, image=image_data)
        return instance
```

`SerializerMethodField`는 모델에 없는 값을 추가하거나 변형하고 싶을 때 사용하는 메소드이다.

```python
# views.py
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
```

`views.py`는 기존과 똑같다.

### 결과

![img](https://velog.velcdn.com/images/mechauk418/post/29f3bb2a-3ac1-4945-a8f2-63070a54e265/image.jpg)

다중 이미지가 업로드되었다.

그런데 DRF에서 제공하는 기본적인 엔드포인트에서는 이미지 파일을 업로드하여 테스트할 수 없다.

postman을 사용하거나 프론트와 연결하여 테스트를 해야한다.

참고 : [Django rest framework 다중 이미지 업로드 방법](https://donis-note.medium.com/django-rest-framework-다중-이미지-업로드-방법-38c99d26258)