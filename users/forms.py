from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.forms import EmailInput
from django.forms import ModelForm, TextInput, EmailInput, CharField, PasswordInput, ChoiceField, BooleanField, \
    NumberInput, DateInput


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class fporegistration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'email', 'phone_number')
        labels = {
            'fpo_name': ('FPO Name'),
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control ",
                'placeholder': 'Enter the First Name',
                'required': 'required',
                "onkeydown" : "return /[a-z]/i.test(event.key)",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter the Last Name',
                'required': 'required',
                "onkeydown" : "return /[a-z]/i.test(event.key)",
            }),
            'email': EmailInput(attrs={
                'class': "form-control ",
                'style': 'max-width: 100%;',
                'placeholder': 'Your Email'
            }),
            'phone_number': TextInput(attrs={
                'type': 'number',
                'maxlength': '10',
                'minlength': '10',
                'class': "form-control ",
                'placeholder': 'Enter your number eg : 12321122',
                'required': 'required',
            }),
        }


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=200)

    class Meta:
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
            })
        }
