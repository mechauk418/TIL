from django.shortcuts import render,redirect

import articles
from .models import Article
from .forms import ArticleForm
from .models import Comment

# Create your views here.


def index(request):
    
    article = Article.objects.order_by('pk')

    context = {

        'articles' : article

    }

    return render(request,'articles/index.html',context)

def create(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect("articles:index")

    else:
        form = ArticleForm()

    context={
        'form':form
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):

    article = Article.objects.get(pk=pk)
    comment = article.comment_set.all()

    context = {
        'article' : article,
        'comment' : comment,
    }

    return render(request,'articles/detail.html', context)

def update(request,pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES ,instance=article)
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

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("articles:index")
    else:
        return redirect("articles:detail", article.pk)
