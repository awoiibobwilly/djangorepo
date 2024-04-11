"""
URL configuration for awoiibobwilly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import index
from aboutus.views import aboutus
from contactus.views import contactus
from blogs.views import blogs
from login.views import login
from register.views import register
from resources.views import resources

urlpatterns = [
    path("", index, name="index"),
    path("aboutus/", aboutus, name="aboutus"),
    path("contactus/", contactus, name="contactus"),
    path("blogs/", blogs, name="blogs"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("resources/", resources, name="resources"),
]
