from email import message
from django.shortcuts import render,redirect
from .models import Comment, Article
from .forms import ArticleForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Model

# Create your views here.

def index(request):

    articles = Article.objects.order_by('pk')
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

def search(request):

    articles = Article.objects.filter(title='')
    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.writer = request.user
            article.save()

            return redirect('articles:index')

    else:
        article_form = ArticleForm()

    context = {
        'article_form' : article_form
    }
    
    return render(request,'articles/create.html',context)

# def detail(request,pk):
#     article = Article.objects.get(pk=pk)
#     comments = article.comment_set.all()
#     if request.method=='POST':
#         comment_form = CommentForm(request.POST, article.pk)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.article = article
#             comment.save()

#         return redirect('articles:detail',article.pk)
#     else:
#         comment_form = CommentForm()

#     context = {
#         'article':article,
#         'comment_form':comment_form,
#         'comments':comments
#     }
#     return render(request,'articles/detail.html', context)

@login_required
def comment_create(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.comment_writer = request.user
        comment.save()

    return redirect('articles:detail',article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    comments_count = article.comment_set.all().count()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'comments_count': comments_count
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comment_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.comment_writer:
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        messages.warning(request,'작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', article_pk)

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.writer:
        if request.method == "POST":
            article.delete()
            return redirect("articles:index")
        else:
            return redirect("articles:detail", article.pk)
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()


def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                return redirect("articles:detail", article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context={
            "article":article,
            'article_form' : article_form,
        }

        return render(request,'articles/update.html',context)

    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()