from django.shortcuts import render
from .models import Todo


def index(request):
    todo_items = Todo.objects.all()
    return render(request,'todo/index.html',{'todo_items':todo_items});
