from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


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


def create_todo(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, "Todo Created Successfully", extra_tags="success")
            return redirect('home')

    else:
        form = TodoCreateForm()
    return render(request, "create.html", {"form": form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "your todo updated successfully", extra_tags="success")
            return redirect('details', todo_id=todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, "update.html", {"form": form})
