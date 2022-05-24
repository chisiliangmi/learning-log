"""learning_logs URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 显示特定主题的详细页面
    path('topics/<topic_id>/', views.topic, name='topic'),
    # 其他用户添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新记录的页面
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # 用于编辑记录的页面
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
