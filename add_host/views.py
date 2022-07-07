from django.shortcuts import render  
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context = {
        'header': 'Главная страница'
    }
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

