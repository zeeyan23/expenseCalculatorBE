from django.urls import path,include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)  

urlpatterns = [
    path('', include(router.urls))
]