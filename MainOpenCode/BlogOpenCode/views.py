from django.shortcuts import render
from django.views.generic.base import View
from BlogOpenCode.models import Post

# Create your views here.

# Вывод записей
from django.views.generic import ListView
from .models import Post


class PostViev(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
