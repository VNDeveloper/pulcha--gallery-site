from django.shortcuts import render, redirect
from django.views import generic
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import LogInForm, UserRegistrationForm
# Create your views here.


def login_view(request):
    template_name = "login/login.html"
    form = LogInForm(request.POST or None)

    if form.is_valid():
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        login(request, user)

    return render(request, template_name, {'form': form})


def register_view(request):
    template_name = "register/register.html"
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.save()
        new_user = authenticate(username=user.email, password=password)
        login(request, new_user)
        return redirect('/')

    return render(request, template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
