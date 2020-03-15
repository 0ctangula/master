from django.contrib import admin
from .models import Profile
from Blog.models import Blog, Blogconf

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blogconf)
admin.site.register(Profile)
