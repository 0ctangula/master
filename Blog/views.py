from django.shortcuts import render, redirect
from Accounts.models import Profile
from .models import Blog, Blogconf
from .models import Comment

# Create your views here.

# Blog Homepage


def blog(request, slug):

    posts = Blog.objects.filter(url=slug)
    blogconf = Blogconf.objects.get(url=slug)

    context = {
        'posts': posts,
        'blogconf': blogconf,
    }

    return render(request,
                  "Blog/blog.html", context)


# Blog Page
def blog_dynamic(request, slug, post):
    if request.method == 'POST':
        # comments
        user = request.user.username
        mainContent = request.POST['mainContent']
        blog = Blog.objects.get(url=post)
        url = blog.url
        comment = Comment(user=user, mainContent=mainContent, url=url)
        comment.save()

    # get information
    blog = Blog.objects.get(url=post)
    customuser = Profile.objects.all()
    suggestion = Blog.objects.all()
    comment = Comment.objects.filter(url=post)
    blogconf = Blogconf.objects.filter(url=slug)

    context = {
        'blogconf': blogconf,
        'customuser': customuser,
        'comment': comment,
        'article':  blog,
        'suggestion': suggestion
    }

    return render(request,
                  "Blog/blog_dynamic.html", context)

# Edit option (only for author)


def blog_edit(request, slug, post):
    obj = Blog.objects.get(url=post)

    if request.method == 'POST':
        obj.delete()

        title = request.POST['title']
        picture = request.POST['picture']
        mainContent = request.POST['mainContent']
        user = obj.user
        date = datetime.datetime.now()
        url = request.POST['url']

        blog = Blog(user=user, title=title, picture=picture,
                    mainContent=mainContent, date=date, url=url)
        blog.save()

        return redirect('/dashboard/')

    context = {
        'object':  obj
    }

    return render(request,
                  "Blog/blog_edit.html", context)

# Delete option(Only for Author)


def blog_delete(request, slug, post):
    obj = Blog.objects.get(url=post)
    if request.method == 'POST':
        obj.delete()
        return redirect('/dashboard/')

    context = {
        'object':  obj
    }

    return render(request,
                  "Blog/blog_delete.html", context)
