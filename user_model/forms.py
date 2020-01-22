from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from tempus_dominus.widgets import DateTimePicker

from .models import UserModel, Message, Tag


class UserModelCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required. Add a valid username')

    class Meta:
        model = UserModel
        fields = ('username', 'fullname', 'role', 'password1', 'password2')


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


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['title', 'tags', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control col-lg-6 col-sm-6'})
        }


class DateRangeForm(forms.ModelForm):
    start_date = forms.DateField(input_formats='%H:%M:%S %d.%m.%Y')
    end_date = forms.DateField(input_formats='%H:%M:%S %d.%m.%Y')

    class Meta:
        model = Message
        fields = ['start_date', 'end_date']

        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
        }
