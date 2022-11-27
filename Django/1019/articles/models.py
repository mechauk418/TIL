from django.db import models
from pjt import settings
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
