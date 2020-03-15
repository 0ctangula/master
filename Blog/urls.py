from django.urls import path
from . import views

urlpatterns = [
    path('blog/<slug:slug>/', views.blog, name="blog"),
    path('blog/<slug:slug>/<slug:post>/',
         views.blog_dynamic, name="blog_dynamic"),
    path('blog/<slug:slug>/<slug:post>/edit/',
         views.blog_edit, name="blog_edit"),
    path('blog/<slug:slug>/<slug:post>/delete/',
         views.blog_delete, name="blog_delete"),
]
