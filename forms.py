from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Location

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_volunteer']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude']
