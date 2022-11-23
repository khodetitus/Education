from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages


# Create your views here.

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {"all": all})


def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', {"todo": todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Todo Deleted Successfully", extra_tags="success")
    return redirect('home')
