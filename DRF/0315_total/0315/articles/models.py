# accounts/models.py
from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hits = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.content
    
class Like(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="like_article"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_like"
    )


class PostImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='image')
    image = ResizedImageField(size=[1000,1000],upload_to="image", null=True, blank=True)
    image_original = models.ImageField(upload_to="image", null=True, blank=True)