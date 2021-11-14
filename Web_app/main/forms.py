from .models import Articles, ServiceForm
from django.forms import ModelForm, TextInput, DateInput, TimeInput, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import DateField
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
# создаем свой класс на модели Articles для бд


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'tel']

        widgets = {
            "name": TextInput(attrs={'placeholder': ''}),
            "tel": TextInput(attrs={'placeholder': ''})
        }


class ServiceFormForm(ModelForm):
    class Meta:
        model = ServiceForm
        fields = ['login', 'name', 'tel', 'type_work', 'date', 'time']

        widgets = {
            # "login": TextInput(attrs={'placeholder': 'логин'}),
            "name": TextInput(attrs={'placeholder': 'Alex', 'class': 'field__input'}),
            "tel": TextInput(attrs={'placeholder': '375(29)9200719-пример', 'class': 'field__input'}),
            "type_work": TextInput(attrs={'placeholder': 'услуга', 'class': 'field__input'}),
            "date": DateInput(attrs={'placeholder': 'дата', 'type': 'date', 'class': 'field__input'}),
            "time": TimeInput(attrs={'placeholder': 'время', 'type': 'time', 'class': 'field__input'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(label="name", required=True)
    tel = forms.CharField(label="tel", required=True)
