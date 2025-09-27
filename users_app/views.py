from django.shortcuts import render, redirect
from .forms import CustomUserRegisterForm
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        register_form = CustomUserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registrierung erfoglreich. Login um zu starten')
            return redirect('todolist')
      
    else:
        register_form = CustomUserRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
        
    
 