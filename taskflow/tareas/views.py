from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render (request, 'tareas/index.html')

def home(request):
    return render (request, 'tareas/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'tareas/home.html'
    context_object_name = 'context'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro')

        if filtro:
            queryset = queryset.filter(tzone__contains=filtro)
        return queryset


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tareas/crear_posteo.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tareas/modificar_posteo.html'
    success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

def cambiar_status(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        post.tzone = 'Completada'
        post.save()
        return redirect('home')
    
def new_status(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status', '')
        post.observations = new_status
        post.save()
        return redirect('home')

