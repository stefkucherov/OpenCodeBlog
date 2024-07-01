from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView
from BlogOpenCode.models import Post
from BlogOpenCode.forms import PostForm
from .models import Post
from .forms import UserRegisterForm
from .forms import PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


# MainOpenCode/views.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        else:
            print(form.errors)  # Вывод ошибок формы в консоль для отладки
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
