from django.shortcuts import render
from django.views.generic.base import View
from BlogOpenCode.models import Post


# Create your views here.

# Вывод записей
class PostViev(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})
