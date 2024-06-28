from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.PostViev.as_view()),
                  path('', views.blog_list, name='blog_list'),
                  path('create/', views.create_post, name='create_post')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
