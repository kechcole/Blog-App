from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserRegisterForm
from django.contrib import messages


def register(request):
    # validate method 
    if request.method == 'POST':
        # Get data 
        form = UserRegisterForm(request.POST)
        # Validate form
        if form.is_valid():
            form.save()    # save infor

            # Success message
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            # Redirect to home page 
            return redirect('blog-home')
        
    # GET method
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})