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
from django.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

from user_model.views import *
from user_model.message_view import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('active-users/', active_users_view, name='active_users'),
    # path('', AllMsgsView.as_view(), name='homepage'),
    path('', find_message_view, name='homepage'),
    path('create-user/', usercreation_view, name='usercreate'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('create/', messagecreate_view, name='create'),
    path('message/<str:slug>/', message_detail, name='message_detail'),
    path('messages/', MessageList.as_view(), name='messages'),
    path('messages-dah/', MessageListDAH.as_view()),
    path('messages-utg/', MessageListUTG.as_view()),
    path('messages-s7/', MessageListS7.as_view()),
    path('messages-bhg/', MessageListBHG.as_view()),
    path('dah/messages-10/', DAHMessageApiView.as_view(), name='dah_messages_api'),
    path('utg/messages-10/', UTGMessageApiView.as_view(), name='utg_messages_api'),
    path('s7/messages-10/', S7MessageApiView.as_view(), name='s7_messages_api'),
    path('bhg/messages-10/', BHGMessageApiView.as_view(), name='bhg_messages_api'),
    path('dah/messages-50/', DAHMsgsView.as_view(), name='dah_messages_obj'),
    path('utg/messages-50/', UTGMsgsView.as_view(), name='utg_messages_obj'),
    path('s7/messages-50/', S7MsgsView.as_view(), name='s7_messages_obj'),
    path('bhg/messages-50/', BHGMsgsView.as_view(), name='bhg_messages_obj'),

    # path('search/', find_message_view, name='find_message'),
    # path('update-user/', user_update_view, name='update-user')
]

urlpatterns = format_suffix_patterns(urlpatterns)
