from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

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


class DateRangeForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d.%m.%Y %H:%M:%S'],
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control mr-sm-2', 'placeholder': 'type date here'}
            # id="id_date" type="text", name="date"
        )
    )

    # <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" name="search">

    # start_date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    # end_date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    # end_date = forms.DateTimeInput()

    # start_date = forms.DateInput(input_formats='%d.%m.%Y %H:%M')
    # end_date = forms.DateInput(input_formats='%d.%m.%Y %H:%M')
    # body_contains = forms.TextInput()

    # class Meta:
    #     model = Message
    #     fields = ['date_pub']
        # fields = ['start_date', 'end_date']
        #
        # widgets = {
        #     'start_date': forms.SelectDateWidget(),
        #     'end_date': forms.SelectDateWidget(),
        #     'body_contains': forms.TextInput(),
        # }
