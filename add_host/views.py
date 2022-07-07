from django.shortcuts import render  
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import HostForm
from .models import Host


def index(request):
    context = {
        'header': 'Главная страница',
    }
    if request.user:
        hosts = request.user.hosts.all()
        context.update({'hosts': hosts})
    return render(request, 'index.html', context)

@csrf_exempt
def signup(request):
    form = UserCreationForm(request.POST or None) 
    if form.is_valid():  
        form.save()
        return redirect('login')

    context = {  
        'form': form,
        'header': 'Регистрация пользователя',
        'button': 'Зарегистрироваться'
    }
    return render(request, 'login.html', context)

@login_required
@csrf_exempt
def add_host(request):
    form = HostForm(request.POST or None)
    if form.is_valid():
        new_host = form.save()
        print(request.user)
        new_host.owners.add(request.user)
        return redirect('index')
    context = {
        'form': form,
        'header': 'Добавить хост',
        'button': 'Добавить'
    }
    return render(request, 'login.html', context)


# @login_required
# @csrf_exempt
# def edit_host(request):
