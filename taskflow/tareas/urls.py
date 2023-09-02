from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView



urlpatterns = [
    path('', views.index, name='index'),
    path('home/', PostListView.as_view(), name='home'),
    path('crear_posteo/', PostCreateView.as_view(), name='crear_posteo'),
    path('modificar_posteo/<pk>/', PostUpdateView.as_view(), name='modificar_posteo'),
    path('eliminar_posteo/<pk>/', PostDeleteView.as_view(), name='eliminar_posteo'),
    path('cambiar_status/<id>/', views.cambiar_status, name='cambiar_status'),
    path('new_status/<id>/', views.new_status, name='new_status'),
    path('tareas_completadas/', views.completed_task_list, name='tareas_completadas'),
]