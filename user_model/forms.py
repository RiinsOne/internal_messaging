from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserModel, Message, Tag, UserRole


class UserModelCreationForm(UserCreationForm):
    # username = forms.CharField(max_length=30, help_text='Required. Add a valid username')
    # role = forms.ModelChoiceField(queryset=UserRole.objects.all())
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserModel
        fields = ('username', 'fullname', 'role', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control col-lg-6 col-sm-6'}),
        }


class UserAutheticationForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login or password')


# class UserUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = UserModel
#         fields = ('username', 'fullname')
#
#     def clean_username(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             try:
#                 user_model = UserModel.objects.exclude(pk=self.instance.pk).get(username=username)
#             except UserModel.DoesNotExist:
#                 return username
#             raise forms.ValidationError('Username "%s" is already in use.' % username)
#
#     def clean_fullname(self):
#         if self.is_valid():
#             fullname = self.cleaned_data['fullname']
#             try:
#                 user_model = UserModel.objects.exclude(pk=self.instance.pk).get(fullname=fullname)
#             except UserModel.DoesNotExist:
#                 return fullname
#             raise forms.ValidationError('Username "%s" is already in use.' % fullname)





class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['title', 'tags', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control col-lg-6 col-sm-6'})
        }
