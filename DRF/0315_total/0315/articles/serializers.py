from rest_framework import serializers
from .models import Article, Comment, Like, PostImage

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    article = serializers.ReadOnlyField(source="articles.pk")

    class Meta:
        model = Comment
        fields = [
            "pk",
            "article",
            "user",
            'userpk',
            'content',
            'created_at',
        ]


class LikeSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source="user.email")
    article = serializers.ReadOnlyField(source="articles.pk")

    class Meta:
        model = Like
        fields = [
            "pk",
            "user",
            "article",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    userpk = serializers.ReadOnlyField(source="user.pk")
    comments = CommentSerializer(many=True, read_only=True)
    like_article = LikeSerializer(many=True, read_only=True)

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
        ]

    
class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = [
            'image',
            'image_original',
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
            ext = str(image_data).split('.')[-1]
            ext = ext.lower()
            if ext in ['jpg', 'jpeg','png',]:
                PostImage.objects.create(article=instance, image=image_data, image_original=image_data)
            elif ext in ['gif','webp']:
                PostImage.objects.create(article=instance, image_original=image_data)
        return instance
