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
            # Implement your password strength logic here
            strength = 10
    else:
        form = PasswordForm()
    return render(request, 'strength_checker/strength_checker.html', {'form': form, 'strength': strength})

# Create your views here.
