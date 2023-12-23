"""dope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import sign_up, user_home, sign_in, sign_out
from django.contrib.auth import views
from .forms import UserLoginForm

urlpatterns = [
    #path('', sign_up, name='front_page'),
    path('home', user_home, name='user_home'),
    path('sign-in', sign_in, name='sign_in'),
    path('sign-up', sign_up, name='sign_up'),
    path('sign-out', sign_out, name='sign_out'), 
    #path('sign-out', sign_out, name='sign_out')
    path('social-auth/', include('social_django.urls', namespace='social'))  
]

