from django.db.models import Q
from django.shortcuts import render
from Blog.models import Blog, Blogconf

# Create your views here.


def search(request):

    blogconf = Blogconf.objects.all()
    blog = Blog.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        blog = blog.filter(
            Q(title__icontains=search_term) | Q(user__icontains=search_term))

    context = {
        'blogconf': blogconf,
        'blog': blog,
        'search_term': search_term,
    }

    return render(request,
                  "Search/index.html", context)
