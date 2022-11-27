from django.shortcuts import render,redirect
from email import message
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request,'articles/index.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        forms = ArticleForm(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form':form
    }

    return render(request,'articles/create.html',context)


def detail(request,pk):

    articles = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments_count = articles.comment_set.all().count()
    comments = articles.comment_set.all()
    context = {
        'articles' : articles,
        'comment_form' : comment_form,
        'comments_count' : comments_count,
        'comments':comments
    }

    return render(request,'articles/detail.html',context)

def delete(request,pk):

    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        if request.method == "POST":
            article.delete()
            return redirect("articles:index")
        else:
            return redirect("articles:detail", article.pk)
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()

@login_required
def create_comment(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()

    return redirect('articles:detail',article.pk)

def comment_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        messages.warning(request,'작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', article_pk)


def update(request,pk):
    articles = Article.objects.get(pk=pk)
    if request.user == articles.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST,instance=articles)
            if form.is_valid():
                form.save()
                return redirect('articles:detail',articles.pk)
        else:
            form = ArticleForm(instance=articles)
        context = {
            'form':form,
            'articles':articles,
        }
        return render(request,'articles/update.html',context=context)

    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()