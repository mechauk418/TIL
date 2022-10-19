from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from articles.models import Article, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    accounts = User.objects.order_by('pk')

    context = {
        'accounts':accounts
    }   

    

    return render(request,'accounts/index.html',context)

def signup(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
        
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()

    context={
        'form':form
    }

    return render(request,'accounts/signup.html',context)


def login(request):

    if request.method=='POST':

        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')

    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }

    return render(request,'accounts/login.html',context)

def detail(request,pk):

    ac_list_detail = User.objects.get(pk=pk)
    article_list = ac_list_detail.article_set.all()
    comment_list = ac_list_detail.comment_set.all()

    context = {
        'ac' : ac_list_detail,
        'article_list':article_list,
        'comment_list':comment_list,
    }

    return render(request,'accounts/detail.html', context)

def update(request):


    if request.method == 'POST':

        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            
        
            return redirect('accounts:index')

    else:
        form = CustomUserChangeForm(instance=request.user)

    context={
        'form':form
    }

    return render(request,'accounts/update.html',context)


def logout(request):


    auth_logout(request)


    return redirect('accounts:index')