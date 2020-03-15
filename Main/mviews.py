###################
####Imports########
###################
from django.shortcuts import render, redirect
from Accounts.models import Profile
from Blog.models import Blog, Blogconf


# Create your views here.

##################
####Home##########
##################
def home(request):

    article = Blog.objects.all()
    blogconf = Blogconf.objects.all()
    profile = Profile.objects.all()

    context = {
        'blogconf': blogconf,
        'article': article,
        'profile': profile
    }

    return render(request,
                  "Main/index.html", context)

# errors


def error401(request):

    return render(request,
                  "Error/401.html",
                  {


                  })

# q-and-a


def qanda(request):

    return render(request,
                  "Main/q-and-a.html",
                  {


                  })
