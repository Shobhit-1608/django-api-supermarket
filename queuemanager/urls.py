from rest_framework.routers import DefaultRouter
from . import views

from django.urls import path, include
from django.urls.resolvers import URLPattern

 
urlpatterns = [
    path('', views.fetch_number, name = "fetch_number")
]
