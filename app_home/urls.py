from django.urls import path
from . import views

urlpatterns = [
     path('', views.home),
     path('app_home/', views.app_home),
]