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
            if len(password) < 8:
                print("Password must be at least 8 characters long.")

            if not re.search("[A-Z]", password):
                 print("Password must contain at least one upper case letter.")

            if not re.search("[a-z]", password):
                print("Password must contain at least one lower case letter")

            if not re.search("[0-9]", password):
                print("Password must contain at least one digit.")

            if not re.search("!@#$%^&*(),.?\":{}|<>", password):
                print("Password must contain at least one special character.")   

            else:
                print("Password is set!")

            strength = 10
    else:
        form = PasswordForm()
    return render(request, 'strength_checker/strength_checker.html', {'form': form, 'strength': strength})

# Create your views here.
