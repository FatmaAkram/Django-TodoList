from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from .models import Todo


def index(request):
    todo_items = Todo.objects.all()
    return render(request,'todo/index.html',{'todo_items':todo_items})


def create(request):
    new_item = Todo(title = request.POST['title'])
    new_item.save()
    return HttpResponseRedirect('/todos/')


def mark_complete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).update(completed=True)
        return JsonResponse({"success": "true"}, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def mark_uncomplete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).update(completed=False)
        return JsonResponse({"success": "true"}, status=200)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
