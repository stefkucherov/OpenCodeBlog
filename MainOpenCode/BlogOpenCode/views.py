from django.shortcuts import render, redirect
from django.views.generic.base import View
from BlogOpenCode.models import Post
from BlogOpenCode.forms import PostForm
# Create your views here.

# Вывод записей
from django.views.generic import ListView
from .models import Post

from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm


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
