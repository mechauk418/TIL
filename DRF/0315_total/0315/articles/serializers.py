from rest_framework import serializers
from .models import Article, Comment, Like, PostImage, Category, Tag

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
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CateTagSerializer(serializers.Serializer):
    cateList = CategorySerializer(many=True)
    tagList = TagSerializer(many=True)
