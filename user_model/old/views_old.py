from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import json as simplejson
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext, loader

from django.views.generic import View

from .models import UserModel, Message, Tag

from .forms import UserModelCreationForm, UserAutheticationForm, MessageForm

from django.conf import settings

from .utils import *


# @login_required(login_url='/login/')
@login_required
def homepage(request):
    users = UserModel.objects.all()
    messages = Message.objects.all()[0:30]
    slug_ne = Message.objects.all().first()
    tags = Tag.objects.all()
    context = {'users': users, 'messages': messages, 'tags': tags}
    lst = range(10)
    context['list'] = lst
    context['slug_ne'] = slug_ne
    return render(request, 'user_model/index.html', context=context)


# class IndexPage(ObjectCreateMessageMixin, View):
#     form_model = MessageForm
#     template = 'user_model/index.html'
#     raise_exception = True

    # another_user = UserModel.objects.filter(username=request.user).first()
    # title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()


@login_required
def usercreation_view(request):
    context = {}
    users = UserModel.objects.all()

    if request.POST:
        form = UserModelCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('homepage')
        else:
            context['usercreation_form'] = form
    else:  # GET request
        form = UserModelCreationForm()
        context['usercreation_form'] = form
        context['users'] = users

    return render(request, 'user_model/usercreationform.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('homepage')

    if request.POST:
        form = UserAutheticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user.is_admin:
                login(request, user)
                settings.SESSION_COOKIE_AGE = 3600
                return redirect('homepage')
            else:
                login(request, user)
                settings.SESSION_COOKIE_AGE = 1800
                return redirect('homepage')

    else:
        form = UserAutheticationForm()

    request.session.set_expiry(0)
    context['login_form'] = form
    return render(request, 'user_model/login.html', context)


@login_required
def messagecreate_view(request):
    another_user = UserModel.objects.filter(username=request.user).first()
    title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()
    current_user = str(request.user).upper()

    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MessageForm({'title': title_info})

    context = {'message_form': form, 'current_user': current_user, 'another_user': another_user}
    return render(request, 'user_model/message_create.html', context)


@login_required
def message_detail(request, slug):
    message = Message.objects.get(slug__iexact=slug)
    return render(request, 'user_model/message_detail.html', context={'message': message})


# def dah_messages_api_view(request):
#     slug_ne = Message.objects.all().first()
#     context = {}
#     lst = range(10)
#     context['list'] = lst
#     context['slug_ne'] = slug_ne
#
#     another_user = UserModel.objects.filter(username=request.user).first()
#     title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()
#
#     if request.POST:
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MessageForm({'title': title_info})
#
#     context['form'] = form
#
#     return render(request, 'user_model/dah_messages_api.html', context=context)


class DAHMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    template = 'user_model/dah_messages_api.html'
