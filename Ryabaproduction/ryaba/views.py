from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm



# Функция регистрации
def regist(request):
    data = {}
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return redirect('re')
    else:
        form = UserCreationForm()
    data['form'] = form
    return render(request, 'ryaba/regist.html', data)

#Главная стр
def main(request):
    return render(request, 'ryaba/main.html')

#Регистрая/Авторизация
def avto(request):
    return render(request, 'ryaba/avto.html')

#Товары магазина
def tovar_myaso(request):
    info = Tovar.objects.all()
    info2 = Tovar_kura.objects.all()
    info3 = Indushation.objects.all()

    ms = {
        'info': info,
        'info2': info2,
        'info3': info3,
    }
    return render(request, 'ryaba/myaso.html', ms)

def tovar_moloko(request):
    info = Sir.objects.all()
    info2 = Moloko.objects.all()
    info3 = Eggs.objects.all()
    info4 = Tvorog.objects.all()

    ms = {
        'info': info,
        'info2': info2,
        'info3': info3,
        'info4': info4,
    }
    return render(request, 'ryaba/moloko.html', ms)

def tovar_posuda(request):
    info = Tarelki.objects.all()
    info2 = Vilki.objects.all()

    ms = {
        'info': info,
        'info2': info2,
    }
    return render(request, 'ryaba/posuda.html', ms)

#ЗАКАЗ
def zakaz(request):
    if request.method == 'POST':
        f = Zakaz2(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            f.save()
            return redirect('oformleno')
    else:
        f = Zakaz2()
    return render(request, 'ryaba/zakaz.html', {'f': f})

# Функция регистрации
def registr(request):
    data = {}
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            data['form'] = form
            return redirect('re')
    else:
        form = UserCreationForm()
    data['form'] = form
    return render(request, 'ryaba/regist.html', data)


#Перенаправление оформления
def oformleno(request):
    return render(request, 'ryaba/oformleno.html')

#Перенаправление регистра
def re(request):
    return render(request, 'ryaba/uspexAvto.html')

#Аутотенфикация
def user_login(request):
    if request.method == 'POST':
        user_login_form = LoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("main")
            else:
                return HttpResponse("Учетная запись или пароль введены неправильно. Пожалуйста, введите заново ~")
        else:
            return HttpResponse("Неверный аккаунт или пароль")
    elif request.method == 'GET':
        user_login_form = LoginForm()
        context = {'form': user_login_form}
        return render(request, 'ryaba/login.html', context)
    else:
        return HttpResponse("Пожалуйста, используйте GET или POST для запроса данных")

def user_logout(request):
    logout(request)
    return render(request, 'ryaba/main.html')