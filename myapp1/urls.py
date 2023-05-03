from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('login/', views.login, name='login'),
    path('home/', views.home_args, name='home'),
    path('home/', views.home, name='home'),


]