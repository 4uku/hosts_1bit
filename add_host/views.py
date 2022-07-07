from django.shortcuts import render  
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

    
def signup(request):
    header = 'Регистрация пользователя'
    form = UserCreationForm(request.POST or None) 
    if form.is_valid():  
        form.save()
        return redirect('index')

    context = {  
        'form': form,
        'header': header
    }
    return render(request, 'signup.html', context)
    