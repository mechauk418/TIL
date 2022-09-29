from turtle import up
from django.shortcuts import render, redirect
from .models import Todo


def index(request):

    posts = Todo.objects.order_by("id")
    context = {"posts": posts}

    return render(request, "todo/index.html", context)


def result(request):

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    created_at = request.GET.get("created_at")
    completed = request.GET.get("completed")

    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
        "created_at": created_at,
        "completed": completed,
    }

    return redirect("todo:index")


def delete(request, pk):

    delete = Todo.objects.get(id=pk)
    delete.delete()

    return redirect("todo:index")


def update(request, pk):

    update = Todo.objects.get(pk=pk)

    if update.completed == True:
        update.completed = False
        update.save()
    else:
        update.completed = True
        update.save()

    return redirect("todo:index")
