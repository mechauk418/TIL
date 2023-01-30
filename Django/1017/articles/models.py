from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from imagekit.processors import ResizeToFit

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField(upload_to ='images/', blank = True )
    thumbnail = ProcessedImageField(
        blank = True,
        processors=[ResizeToFit(200,200)],
        format='JPEG',
        options={'quality':90},
    )


class Comment(models.Model):

    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)