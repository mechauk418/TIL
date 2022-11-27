from rest_framework import serializers
from post.models import Post  # Article 모델 받아오기


# 모델을 기반으로 Serializer 만들기
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # 모델이 Article 모델이다.
        fields = "__all__" # 모든 필드를 다 다루겠다.

        