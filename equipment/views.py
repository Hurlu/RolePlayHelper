from django.shortcuts import render, redirect
from .forms import LoginForm
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def IndexView(request):
    if request.user.is_authenticated():
        pass
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['login']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                else:
                    render(request, "equipment/index.html", context={'form': form})
                render(request, "equipment/index.html")
            else:
                render(request, "equipment/index.html", context={'form': form})
        form = LoginForm()
        return render(request, "equipment/index.html", context={'form': form})

def LogoutView(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/')