from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/settings/', views.settings, name="settings"),
    path('dashboard/profile/', views.profile, name="profile"),
    # Blog concerning stuff
    path('dashboard/blog/<slug:slug>/config/',
         views.blog_conf, name="blog_conf"),
    path('dashboard/blog/<slug:slug>/post/',
         views.blog_post, name="blog_post"),
    path('dashboard/blog/', views.blog_main, name="blog_main"),
    path('dashboard/blog/<slug:slug>/', views.blog_details, name="blog_details"),
    path('dashboard/developers/', views.developers, name="developers"),
    path('dashboard/new-blog/', views.new_blog, name='new_blog'),
    # collaboration teams
    path('dashboard/blog/<slug:slug>/invite/', views.invite, name="invite"),
    # register
    path('register/', views.register, name="register"),
    # user page
    path('user/<slug:slug>/', views.user, name="user"),
]
