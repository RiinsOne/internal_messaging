from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from socket import gethostname
from datetime import datetime


class ObjectCreateMessageMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
        return render(request, self.template, context={'form': bound_form})


class ObjectMessagesApiMixin:
    template = 'user_model/ten_messages_api.html'
    db_model = UserModel
    form_model = MessageForm
    db_msg = Message
    tag_arg = None

    def get(self, request):
        lst = range(10)
        slug_ne = self.db_msg.objects.filter(tags__title=self.tag_arg).first()

        hostname = gethostname()
        another_user = self.db_model.objects.filter(username=request.user).first()
        title_info = str(another_user).upper() + ', ' + str(hostname).upper()

        form = self.form_model({'title': title_info})
        context = {'list': lst, 'slug_ne': slug_ne, 'form': form, 'tag_arg': self.tag_arg, 'block_title': self.tag_arg + ' last 10 messages'}
        return render(request, self.template, context=context)

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return HttpResponseRedirect('')
        context={'form': bound_form}
        return render(request, self.template, context=context)


class ObjectMsgsViewMixin:
    template = 'user_model/fifty_msgs_template.html'
    tag_arg = None

    def get(self, request):
        dah_backoffice = UserRole.objects.get(title='DAH-BACKOFFICE')
        users_backoffice = UserModel.objects.filter(role=dah_backoffice)
        

        if self.tag_arg is not None:
            messages = Message.objects.filter(tags__title=self.tag_arg)[:50]
            return render(request, self.template, context={'messages': messages, 'block_title': self.tag_arg + ' last 50 messages', 'users_backoffice': users_backoffice})
        messages = Message.objects.all()[:50]
        return render(request, 'user_model/main_page.html', context={'messages': messages})

    def post(self, request):
        pass
