import sys
from django.db import models


class Director(models.Model):
    name = models.TextField(max_length=30)
    debut = models.DateTimeField()
    country = models.TextField(max_length=30)

class Genre(models.Model):
    title = models.TextField(max_length=30)

