from dataclasses import fields
from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title','content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글')
    
    class Meta:
        model = Comment
        fields = ('content',)
