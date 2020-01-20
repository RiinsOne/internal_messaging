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
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('username', 'password')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control col-lg-4 col-sm-6 col-8 justify-content-center'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control col-lg-4 col-sm-6 col-8 justify-content-center'})
        # }
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


class MessageForm(forms.ModelForm):
    # tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    # )

    class Meta:
        model = Message
        fields = ['title', 'tags', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control col-lg-6 col-sm-6'})
        }
