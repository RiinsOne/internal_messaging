from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


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
    template = None
    db_model = UserModel
    form_model = MessageForm
    db_msg = Message
    tag_arg = None

    def get(self, request):
        lst = range(10)
        slug_ne = self.db_msg.objects.filter(tags__title=self.tag_arg).first()

        another_user = self.db_model.objects.filter(username=request.user).first()
        title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()

        form = self.form_model({'title': title_info})
        context = {'list': lst, 'slug_ne': slug_ne, 'form': form}
        return render(request, self.template, context=context)

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return HttpResponseRedirect('')
        context={'form': bound_form}
        return render(request, self.template, context=context)
