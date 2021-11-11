import instance as instance
from django.shortcuts import render, redirect
from .forms import ArticlesForm, ServiceFormForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import CreateUserForm
from django.contrib import messages, auth

from .models import ServiceForm

from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm




# Для личного кабинета поиск удаление и редактирование записей
class checkInfo(DetailView):
    model = ServiceForm
    template_name = 'main/detail-view.html'
    context_object_name = 'service'

class updateInfo(UpdateView):
    model = ServiceForm
    template_name = 'main/form.html'
    form_class = ServiceFormForm

class deleteInfo(DeleteView):
    model = ServiceForm
    success_url = '/personalAccount/'
    template_name = 'main/deleteInfo.html'

# вывод информации о записи
def personalAccount(request):
    info = ServiceForm.objects.filter(login=request.user.id).all()
    # info = ServiceForm.objects.all()
    return render(request, 'main/personalAccount.html', {'info': info})



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'main/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def exit(request):
    logout(request)
    return redirect('main')

# Оправить заявку на звонок
def main(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            try:
                send_mail(f"Заявка от {name}", str(tel),
                          'elhom99@gmail.com', ['elhom99@gmail.com'])
                form = ArticlesForm()
                data = {
                    'form': form,
                    'var': 1
                }
                return render(request, 'main/main.html', data)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
        else:
            messages.info(request, 'Форма была неверной')
            return redirect('http://127.0.0.1:8000/#register')


    form = ArticlesForm()
    data = {
        'form': form,
        'error': error

    }
    return render(request, 'main/main.html', data)

#Окно сообщения
# def message(request):
#     form = ArticlesForm(request.POST)
#     if form.is_valid():
#         messages.info(request, 'Ваша заявка одобренно, с вами свяжется наш менеджер!')
#         return render(request, 'main/main.html', {'var': 1})
#     else:
#         messages.info(request, 'Форма была неверной')
#         return redirect('http://127.0.0.1:8000/#register')

# запись на услугу
def form1(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == "POST":
            form = ServiceFormForm(request.POST)
            if form.is_valid():
                # form.login = request.user
                form.save()
                return redirect('main')
            else:
                error = "Форма была неверной"

        form = ServiceFormForm()
        data = {
            'form': form,
            'error': error

        }
        return render(request, 'main/form.html', data)
    else:
        messages.info(request, "Для записи вам необходимо войти в свой личный кабинет!")
        return redirect('login')




