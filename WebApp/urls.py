"""
Definition of urls for WebApp.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Main import mviews
from Search import sviews


urlpatterns = [
    ####Login & Registration#####
    #############################
    path('', include('django.contrib.auth.urls')),
    #############################
    ###########Dashboard#########
    #############################
    path('', include('Accounts.urls')),
    #############################
    ##########Search#############
    #############################
    path('search/', sviews.search, name='search'),
    #############################
    ##########Blog###############
    #############################
    path('', include('Blog.urls')),
    #############################
    ########General URLS#########
    #############################
    path('', mviews.home, name="home"),
    path('q-and-a/', mviews.qanda, name="qanda"),
    path('admin/', admin.site.urls),
    #############################
    ##########Errors#############
    #############################
    #############################
    path('error401/', mviews.error401, name="error401"),
    #############################
    ##########Rest API###########
    #############################
    path('', include('RestAPI.urls')), ]
