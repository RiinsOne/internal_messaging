from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserModel, Message, Tag


class UserModelCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required. Add a valid username')

    class Meta:
        model = UserModel
        fields = ('username', 'fullname', 'entity', 'password1', 'password2')


class UserAutheticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login or password')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
