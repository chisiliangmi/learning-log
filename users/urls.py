"""Users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views


urlpatterns = [
    # 登陆页面
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'),
    # 注销页面
    path('logout/', views.logout_view, name='logout'),
    # 注册页面
    path('register', views.register, name='register')
]
