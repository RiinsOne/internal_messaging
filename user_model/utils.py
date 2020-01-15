from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class ObjectCreateMessageMixin:
    form_model = None
    template = None
    # title_info = None

    # another_user = UserModel.objects.filter(username=request.user).first()
    # title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()

    def get(self, request):
        # form = self.form_model({'title': title_info})
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
        return render(request, self.template, context={'form': bound_form})


# def messagecreate_view(request):
#     another_user = UserModel.objects.filter(username=request.user).first()
#     title_info = str(another_user).upper() + ' \\\ ' + str(another_user.entity).upper()
#     current_user = str(request.user).upper()
#
#     if request.POST:
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     else:
#         form = MessageForm({'title': title_info})
#
#     context = {'message_form': form, 'current_user': current_user, 'another_user': another_user}
#     return render(request, 'user_model/message_create.html', context)
