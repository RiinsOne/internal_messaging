"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from rest_framework.urlpatterns import format_suffix_patterns

from user_model.views import *
from user_model.message_view import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    # path('', IndexPage.as_view(), name='homepage'),
    path('usercreate/', usercreation_view, name='usercreate'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('create/', messagecreate_view, name='create'),
    path('message/<str:slug>/', message_detail, name='message_detail'),
    path('messages/', MessageList.as_view()),
    path('messages-dah/', MessageListDAH.as_view()),
    path('messages-utg/', MessageListUTG.as_view()),
    path('messages-s7/', MessageListS7.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
