###############
###Imports#####
###############
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from Blog.models import Blogconf, Blog
import datetime


#############
##register###
#############
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {
                      'form': form
                  })
#############
##Dashboard##
#############


def dashboard(request):
    username = request.user

    obj = Blog.objects.filter(user=username)  # Blog Posts
    follower = Profile.objects.all()

    context = {
        'object':  obj,
        'follower': follower,
    }

    return render(request,
                  "dashboard/index.html", context)

# profile


def profile(request):

    username = request.user
    profile = Profile.objects.filter(user=username)
    if request.method == 'POST':
        profile.delete()

        username = request.POST['username']
        picture = request.POST['picture']
        description = request.POST['description']
        profilepicture = request.POST['profilepicture']

        usersettings = Profile(user=username, picture=picture,
                               description=description, profilepicture=profilepicture)
        usersettings.save()

        return redirect('/dashboard/profile')

    context = {
        'profile': profile,
        'username': username,

    }

    return render(request,
                  "dashboard/profile.html",
                  context)


# settings
def settings(request):

    return render(request,
                  "dashboard/settings.html",)

############
###Blogs####
############

# View of all existing Blogs on that account


def blog_main(request):

    blog = Blogconf.objects.filter(user=request.user)

    context = {
        'blog': blog,

    }

    return render(request, 'dashboard/blog_main.html', context)


def new_blog(request):
    blog = Blogconf.objects.all()
    profile = Profile.objects.filter(user=request.user)

    if request.method == 'POST':
        blogconf = Blogconf.objects.all()
        user = request.user.username
        title = request.POST['title']
        picture = request.POST['picture']
        description = request.POST['description']
        unformatedurl = request.POST['url']
        url = unformatedurl.replace(' ', '-')

        blogconf = Blogconf(user=user, title=title,
                            picture=picture, description=description, url=url)
        blogconf.save()

        return redirect('/dashboard/blog/')

    context = {
        'profile': profile,
    }
    return render(request, 'dashboard/new_blog.html', context)

# View of one single Blog (including posts etc.)


def blog_details(request, slug):
    blog = Blog.objects.all()
    blogconf = Blogconf.objects.get(url=slug)

    context = {
        'blog': blog,
        'blogconf': blogconf,
    }

    return render(request, 'dashboard/blog_details.html', context)

# blog post


def blog_post(request, slug):
    ############
    #save#to#db#
    ############
    date = datetime.date.today()
    formateddate = date.strftime("%d %b %Y")

    if request.method == 'POST':
        title = request.POST['title']
        picture = request.POST['picture']
        mainContent = request.POST['mainContent']
        user = request.user
        date = formateddate
        unformatedurl = request.POST['title']
        url = unformatedurl.replace(' ', '-')
        blogconf = Blogconf.objects.get(user=request.user)
        blogtitle = blogconf.url

        blog = Blog(user=user, title=title, picture=picture,
                    mainContent=mainContent, date=date, url=url, blogtitle=blogtitle)
        blog.save()

        return redirect('/dashboard/blog/')

    post = Blog.objects.filter(user=request.user)
    blogconf = Blogconf.objects.filter(url=slug)
    profile = Profile.objects.filter(user=request.user)

    context = {
        'blogconf': blogconf,
        'post': post,
        'profile': profile
    }

    return render(request,
                  "dashboard/blog_post.html", context)

# blog configuration


def blog_conf(request, slug):
    profile = Profile.objects.filter(user=request.user)
    blogconf = Blogconf.objects.filter(user=request.user)

    if request.method == 'POST':
        blogconf.delete()

        user = request.user.username
        title = request.POST['title']
        picture = request.POST['picture']
        description = request.POST['description']

        blogconf = Blogconf(user=user, title=title,
                            picture=picture, description=description)
        blogconf.save()

        return redirect('/dashboard/blog/config/')

    context = {
        'profile': profile,
        'blogconf': blogconf,
    }

    return render(request,
                  "dashboard/blog_conf.html", context)


##########
###User###
##########
def user(request, slug):

    customuser = Profile.objects.get(user=slug)
    article = Blog.objects.filter(user=slug)

    context = {
        'article': article,
        'customuser': customuser,

    }

    return render(request,
                  "user/index.html",
                  context)

#############
###Devs######
############


def developers(request):

    return render(request,
                  "dashboard/developers.html",)


###########
####Join###
###########

def invite(request, slug):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request,
                  "dashboard/invite.html", context,)
