
from django.urls import include, path
from rest_framework import routers
from . import views

###########
##routers##
###########

router = routers.DefaultRouter()
router.register(r'Blog', views.BlogViewSet)


urlpatterns = [path('api/', include(router.urls)),
               path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
