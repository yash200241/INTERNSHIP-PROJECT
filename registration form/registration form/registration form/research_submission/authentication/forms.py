# authentication/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User  # Add this line

class LoginForm(AuthenticationForm):
    # Add any additional customization to the login form if needed
    pass

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User  # Use the imported User model
        fields = ['username', 'email', 'password1', 'password2']
        
