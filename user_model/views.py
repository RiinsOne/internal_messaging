from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .models import UserModel, Message, Tag

from .forms import UserModelCreationForm, UserAutheticationForm, MessageForm


def homepage(request):
    users = UserModel.objects.all()
    messages = Message.objects.all()
    tags = Tag.objects.all()
    context = {'users': users, 'messages': messages, 'tags': tags}
    return render(request, 'user_model/index.html', context=context)


def usercreation_view(request):
    context = {}

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

            if user:
                login(request, user)
                return redirect('homepage')

    else:
        form = UserAutheticationForm()

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
