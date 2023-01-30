from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title','content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글')
    
    class Meta:
        model = Comment
        fields = ('content',)
