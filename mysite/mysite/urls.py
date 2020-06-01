from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('todos/', views.index),
    path('todos/new', views.create),
    path('todos/complete', views.mark_complete),
    path('todos/uncomplete', views.mark_uncomplete),
    path('todos/delete',views.delete ),
]
