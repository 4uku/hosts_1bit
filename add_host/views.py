from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import Host
from .utils import form_for_user


def index(request):
    context = {
        'header': 'Главная страница',
    }
    if not request.user.is_anonymous:
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
    form = form_for_user(request.user)(request.POST or None)
    if form.is_valid():
        new_host = form.save()
        if not request.user.is_staff:
            new_host.owners.add(request.user)
        return redirect('index')
    context = {
        'form': form,
        'header': 'Добавить хост',
        'button': 'Добавить'
    }
    return render(request, 'login.html', context)


@login_required
@csrf_exempt
def edit_host(request, host_id):
    host = get_object_or_404(Host, id=host_id)
    if request.user not in host.owners.all() and not request.user.is_staff:
        return redirect('index')
    form = form_for_user(request.user)(request.POST or None, instance=host)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'header': 'Редактирование хоста',
        'button': 'Изменить',
        'form': form
    }
    return render(request, 'login.html', context)


@login_required
def all_hosts(request):
    if not request.user.is_staff:
        return redirect('index')
    hosts = Host.objects.all()
    context = {
        'header': 'Все хосты',
        'hosts': hosts
    }
    return render(request, 'index.html', context)
