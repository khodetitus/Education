from django.shortcuts import render
from .models import Todo


# Create your views here.

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {"all": all})


def say_hello(request):
    person = {"name": "masoud"}
    return render(request, 'hello.html', context=person)


