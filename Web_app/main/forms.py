from .models import Articles, ServiceForm
from django.forms import ModelForm, TextInput, DateInput, TimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# создаем свой класс на модели Articles для бд


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'tel']

        widgets = {
            "name": TextInput(attrs={'placeholder': 'имя'}),
            "tel": TextInput(attrs={'placeholder': 'телефон'})
        }


class ServiceFormForm(ModelForm):

    class Meta:
        model = ServiceForm
        fields = ['login', 'name', 'tel', 'type_work', 'date', 'time']

        widgets = {
            # "login": TextInput(attrs={'placeholder': 'логин'}),
            "name": TextInput(attrs={'placeholder': 'имя'}),
            "tel": TextInput(attrs={'placeholder': 'телефон'}),
            "type_work": TextInput(attrs={'placeholder': 'услуга'}),
            "date": DateInput(attrs={'placeholder': 'дата'}),
            "time": TimeInput(attrs={'placeholder': 'время'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(label="name", required=True)
    tel = forms.CharField(label="tel", required=True)