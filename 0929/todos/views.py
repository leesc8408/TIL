from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import todo

# Create your views here.
def index(request):
    todos_ = todo.objects.all()
    context = {
        "todos": todos_,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content_")
    priority = request.GET.get("priority_")
    deadline = request.GET.get("deadline_")
    todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )
    return redirect("todos:index")


def delete(request, todo_id):
    todo_ = todo.objects.get(id=todo_id)
    todo_.delete()
    return redirect("todos:index")


def update(request, pk):
    todo_ = todo.objects.get(id=pk)
    todo_.completed = not todo_.completed
    todo_.save()
    return redirect("todos:index")
