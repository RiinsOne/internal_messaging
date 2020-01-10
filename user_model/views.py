from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
import json as simplejson
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext, loader

from .models import UserModel, Message, Tag

from .forms import UserModelCreationForm, UserAutheticationForm, MessageForm

from django.conf import settings


def homepage(request):
    users = UserModel.objects.all()
    messages = Message.objects.all()
    tags = Tag.objects.all()
    context = {'users': users, 'messages': messages, 'tags': tags}
    return render(request, 'user_model/index.html', context=context)


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
    return redirect('homepage')


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


def message_detail(request, slug):
    message = Message.objects.get(slug__iexact=slug)
    return render(request, 'user_model/message_detail.html', context={'message': message})


# def index(request):
#     return HttpResponse(loader.get_template('user_model/api.html').render(RequestContext(request,{'latest_results_list': Message.objects.all()})))
#
#
# def update(request):
#      results = [ob.as_json() for ob in Results.objects.all()]
#      return JsonResponse({'latest_results_list':results})

# https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python/2428119#2428119
def api_view(request):
    messages = Message.objects.all()

    api_dict = {}

    lst_title = []
    for m in messages:
        lst_title.append(m.title)

    lst_tags = []
    for m in messages:
        tml_lst = []
        for t in m.tags.all():
            tml_lst.append(t.title)
        lst_tags.append(tml_lst)

    lst_body = []
    for m in messages:
        lst_body.append(m.body)

    zip_lst = list(zip(lst_title, lst_tags, lst_body))

    for char in range(len(zip_lst)):
        api_dict[char] = zip_lst[char]

    data = simplejson.dumps(api_dict)

    # return render(request, 'user_model/api.html', context={'api_dict': api_dict})
    return HttpResponse(data, content_type='application/json')
