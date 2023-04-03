from django.contrib import admin
from .models import Tag, Category, Comment
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)

