from rest_framework import serializers
from .models import Article, Comment, Like

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
        ]

