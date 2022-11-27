from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, "front/index.html")


def create(request):

    return render(request,"front/create.html")

def detail(request,pk):

    return render(request,"front/detail.html")
