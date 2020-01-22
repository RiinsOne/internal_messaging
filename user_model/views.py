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

from socket import gethostname


class AllMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = None


class DAHMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'DAH'


class UTGMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'UTG'


class S7MsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'S7'


class BHGMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'BHG'


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
    else:
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
    hostname = gethostname()
    another_user = UserModel.objects.filter(username=request.user).first()
    title_info = str(another_user).upper() + ', ' + str(hostname).upper()
    current_user = str(request.user).upper()

    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MessageForm({'title': title_info})

    context = {'message_form': form, 'current_user': current_user, 'another_user': another_user}
    context['hostname'] = hostname
    return render(request, 'user_model/message_create.html', context)


@login_required
def message_detail(request, slug):
    message = Message.objects.get(slug__iexact=slug)
    return render(request, 'user_model/message_detail.html', context={'message': message})


class DAHMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'DAH'


class UTGMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'UTG'


class S7MessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'S7'


class BHGMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'BHG'
