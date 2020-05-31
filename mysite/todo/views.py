from django.shortcuts import render
from django.http import  JsonResponse
from .models import Todo


def index(request):
    todo_items = Todo.objects.all()
    return render(request,'todo/index.html',{'todo_items':todo_items})


def create(request):
    item = Todo.objects.create(title = request.POST['title'])
    return JsonResponse({
        'id': item.id,
        'title': item.title,
        'completed': item.completed
    }, status=200)


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
    return JsonResponse({"error": ""}, status=400)


def delete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).delete()
        return JsonResponse({"success": "true"}, status=200)
    return JsonResponse({"error": ""}, status=400)