from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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


# Render a profile template
@login_required
def profile(request):

    # If this is a POST request
    if request.method == 'POST':
        # Create form 
        u_form = UserUpdateForm(request.POST,           # Get post data 
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,       # Get file data, here is the image
                                   instance=request.user.profile)
    
        # Validate data 
        if u_form.is_valid() and p_form.is_valid():
            # If valid save data 
            u_form.save()
            p_form.save()

            # Notify user of success data capture 
            messages.success(request, f'Thanks {request.user.username} Your account is upto date!')
            # Send get request to reload profile page 
            return redirect('profile')
            
    
    # Not a POST request
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    # Pass forms to the template using a context
    context = {
        'u_form':u_form,
        'p_form': p_form
    }


    # Pass context to the html template
    return render(request, 'users/profile.html', context)