# [DRF] 이미지 업로드 관련 옵션 - 리사이징, 확장자 제한



일반적인 웹페이지에서 이미지는 용량의 큰 비중을 차지한다.

용량이 큰 이미지파일은 DB 공간도 많이 먹고, 서비스 이용자에게 불쾌한 로딩을 경험시킨다.

[비트윈에서 서버 비용을 70%나 줄인 온디맨드 리사이징 이야기
](https://blog-tech.tadatada.com/2016-05-16-ondemand-image-resizing)

위 글은 커플을 위한 어플인 비트윈에서 리사이즈로 서버 비용을 절약한 사례인데, 리사이징의 필요성을 알 수 있다.

그리고 이미지 파일에 확장자 제한을 하는 것은 악성 파일을 막는 것에 큰 도움이 된다.

[다중 이미지 업로드하기](https://velog.io/@mechauk418/DRF-%EB%8B%A4%EC%A4%91-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0) 

위 코드를 간단하게 수정하여 리사이징, 확장자 제한을 해보았다.

리사이징에는 `django-resized` 라는 라이브러리를 사용했다.

### 코드

```python
# 라이브러리 설치하기
pip install django-resized
```

```python

# models.py

from django_resized import ResizedImageField


class PostImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='image')
    image = ResizedImageField(size=[1000,1000],upload_to="image", null=True, blank=True)
    image_original = models.ImageField(upload_to="image", null=True, blank=True)

```

`image` 필드를 `ResizedImageField`로 바꿔주고 `image_original` 이라는 이미지 원본 필드를 추가하였다.

`ResizedImageField`는 가로, 세로의 최대 이미지를 제한하여 만약 가로나 세로가 그 제한을 초과하면 원본 비율을 유지하면서 리사이징해준다.


```python

# serializers.py

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
            ext = str(image_data).split('.')[-1] # ext에 확장자 명이 담긴다.
            ext = ext.lower() # 확장자를 소문자로 통일
            if ext in ['jpg', 'jpeg','png',]:
                PostImage.objects.create(article=instance, image=image_data, image_original=image_data)
            elif ext in ['gif','webp']:
                PostImage.objects.create(article=instance, image_original=image_data)
        return instance

```

확장자 제한는 파일에서 확장자 명을 추출하여 원하는 확장자만 통과시켜 저장하는 방식을 사용했다.

이렇게 간단한 이미지 업로드 옵션을 설정했다.

그런데 테스트해보니 문제가 발생했다.

`django-resized`가 gif, webp를 지원하지 않는다.

gif는 리사이징은 하는데 재생이 안되며 webp는 아예 DB에 담지 못했다.

그래서 일반적인 이미지 확장자 (jpg, jpeg, png)는 원본과 리사이징을 모두 저장했고,

gif와 webp는 원본만 저장하고 리사이징하지 않았다.

아쉽지만 프론트에서 리사이징 이미지가 없으면 원본을 출력하고 리사이징 이미지가 있으면 리사이징 이미지를 출력하는 식으로 문제를 해결했다.