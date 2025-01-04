import re

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PasswordForm

def index(request):
    print("why are you here")
    return HttpResponse("started...")

def check_password(request):
    strength = None
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            strength = 100
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                strength -= 20

            if not re.search("[A-Z]", password):
                print("Password must contain at least one upper case letter.")
                strength -= 20

            if not re.search("[a-z]", password):
                print("Password must contain at least one lower case letter")
                strength -= 20

            if not re.search("[0-9]", password):
                print("Password must contain at least one digit.")
                strength -= 20

            if not re.search("!@#$%^&*(),.?\":{}|<>", password):
                print("Password must contain at least one special character.")
                strength -= 20   

            else:
                print("Password is set!")

            
    else:
        form = PasswordForm()
    return render(request, 'strength_checker/strength_checker.html', {'form': form, 'strength': strength})

# Create your views here.
