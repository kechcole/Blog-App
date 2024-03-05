from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    # validate method 
    if request.method == 'POST':
        # Get data 
        form = UserRegisterForm(request.POST)
        # Validate form
        if form.is_valid():
            form.save()    # save user data 

            # Success message
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, You have successfully been verified, procced to login!')
            
            # Redirect to home page 
            return redirect('login')
        
    # GET method
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})