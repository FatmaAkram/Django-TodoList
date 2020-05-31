from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo


def index(request):
    todo_items = Todo.objects.all()
    return render(request,'todo/index.html',{'todo_items':todo_items})

def create(request):
    new_item = Todo(title = request.POST['title'])
    new_item.save()
    return HttpResponseRedirect('/todos/')