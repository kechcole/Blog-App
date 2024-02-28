from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    # validate method 
    if request.method == 'POST':
        # Get data 
        form = UserCreationForm(request.POST)
        # Validate form
        if form.is_valid():
            form.save()    # save user data 

            # Success message
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            # Redirect to home page 
            return redirect('blog-home')
        
    # GET method
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})