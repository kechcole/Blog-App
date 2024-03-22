from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Inherit from user form and add fields 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Specify model to use
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Convert User model to form 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    # Fields in the model that should be used. 
    class Meta:
        model = User
        fields = ['username', 'email']



# Image field form
class ProfileUpdateForm(forms.ModelForm):

    # Field
    class Meta:
        model = Profile
        fields = ['image']



