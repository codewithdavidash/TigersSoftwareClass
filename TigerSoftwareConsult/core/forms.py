from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


INPUT_STYLES = """
padding: 5px;
height: 40px;
"""

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Your username...',
          'style': INPUT_STYLES
     }))
     password = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Your password...',
          'style': INPUT_STYLES
     }))
class SignupForm(UserCreationForm):
     class Meta:
          model = User
          fields = ('username', 'email', 'password1', 'password2')
     username = forms.CharField(widget=forms.TextInput(attrs={
          'placeholder': 'Your username...',
          'style': INPUT_STYLES
     }))
     email = forms.CharField(widget=forms.EmailInput(attrs={
          'placeholder': 'Your email...',
          'style': INPUT_STYLES
     }))
     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Your password...',
          'style': INPUT_STYLES
     }))
     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
          'placeholder': 'Your password confirmation...',
          'style': INPUT_STYLES
     }))
