from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.views.generic import View
from django.conf import settings

from .models import UserModel, Message, Tag
from .forms import UserModelCreationForm, UserAutheticationForm, MessageForm
from .utils import *
from .datetime_formatter import dt_formatter, q_delta, randtime, randdate
from datetime import datetime, timedelta

from socket import gethostname


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
def mainpage_view(request):
    context = {}

    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    if start_date and end_date:
        try:
            messages = Message.objects.filter(
                date_pub__gte=dt_formatter(start_date),
                date_pub__lte=dt_formatter(end_date)
            )
            context['messages'] = messages
        except:
            allert = 'Введите корректные данные!'
            context['allert'] = allert
        context['sd'] = start_date
        context['ed'] = end_date
    else:
        warning = 'Для поиска нужно заполнить все поля формы.'
        context['warning'] = warning

    return render(request, 'user_model/main_page.html', context=context)


def find_message_view(request):
    context = {}
    random_date = randdate()
    start_randtime = randtime(0, 11)
    end_randtime = randtime(12, 24)
    context['random_date'] = random_date
    context['start_randtime'] = start_randtime
    context['end_randtime'] = end_randtime

    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    if start_date == '' and end_date == '':
        context['allert_info'] = 'Для поиска нужно заполнить все поля формы.'
    elif start_date.upper().isupper() == True or end_date.upper().isupper() == True:
        context['alpha_error'] = 'Поля не должны содержать буквы.'
    elif start_date.upper().isupper() == False and end_date.upper().isupper() == False:
        try:
            if q_delta(start_date, end_date):
                messages = Message.objects.filter(
                    date_pub__gte=dt_formatter(start_date),
                    date_pub__lte=dt_formatter(end_date)
                )
                context['messages'] = messages
                context['sd'] = start_date
                context['ed'] = end_date
            else:
                context['delta_error'] = 'Указанный период превышает двое суток!'
        except:
            context['type_error'] = 'Введен неправильный формат даты и времени!'
    else:
        pass

    return render(request, 'user_model/find_message.html', context=context)


@login_required
def message_detail(request, slug):
    message = Message.objects.get(slug__iexact=slug)
    return render(request, 'user_model/message_detail.html', context={'message': message})


# --------------------------------------------------


class DAHMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'DAH'


class UTGMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'UTG'


class S7MessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'S7'


class BHGMessageApiView(LoginRequiredMixin, ObjectMessagesApiMixin, View):
    tag_arg = 'BHG'


# --------------------------------------------------


# class AllMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
#     tag_arg = None


class DAHMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'DAH'


class UTGMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'UTG'


class S7MsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'S7'


class BHGMsgsView(LoginRequiredMixin, ObjectMsgsViewMixin, View):
    tag_arg = 'BHG'
