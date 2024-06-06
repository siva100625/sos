from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import LocationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegisterForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Assuming 'home' is the name of your home page URL
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Assuming 'home' is the name of your home page URL
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LocationForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def share_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.user = request.user
            location.save()

            # Send email to all volunteers
            volunteers = CustomUser.objects.filter(is_volunteer=True)
            recipient_emails = [volunteer.email for volunteer in volunteers]
            subject = 'SOS Alert: Location Shared'
            message = f'https://maps.google.com/?q={location.latitude},{location.longitude}'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, recipient_emails)

            return redirect('home')
    else:
        form = LocationForm()
    return render(request, 'myapp/share_location.html', {'form': form})

def home(request):
    return render(request, "myapp/home.html")

