import re

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PasswordForm

def index(request):
    print("why are you here")
    return HttpResponse("started...")

def check_password(request):
    strength = None
    strings = []
    length = 0
    if request.method == 'POST':
        
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            strength = 100
            if len(password) < 8:
                strings.append("Password must be at least 8 characters long.")
                print("Password must be at least 8 characters long.")
                strength -= 20

            if not re.search("[A-Z]", password):
                strings.append("Password must contain at least one upper case letter.")
                print("Password must contain at least one upper case letter.")
                strength -= 20

            if not re.search("[a-z]", password):
                strings.append("Password must contain at least one lower case letter")
                print("Password must contain at least one lower case letter")
                strength -= 20

            if not re.search("[0-9]", password):
                strings.append("Password must contain at least one digit.")
                print("Password must contain at least one digit.")
                strength -= 20

            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                strings.append("Password must contain at least one special character.")
                print("Password must contain at least one special character.")
                strength -= 20   

            else:
                strings.append("Password is set!")
                print("Password is set!")

            length = len(strings)
            

    
    else:
        form = [PasswordForm()]
    return render(request, 'strength_checker/strength_checker.html', {'form': form, 'strength': strength, 'strings': strings, 'length': length})

# Create your views here.
