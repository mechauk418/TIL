from django.db import models
from accounts.models import User
from pjt import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Comment(models.Model):

    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    comment_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
