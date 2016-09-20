from django.shortcuts import render, redirect
from .forms import LoginForm
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from equipment.models import *


def CharacterView(request):
    if not request.user.is_authenticated():
        redirect('/')
    if request.user.username != "admin":
        char = Player.objects.filter(user_id=request.user.id).first()
        if char is None:
            return HttpResponse("Ha le MJ il t'a pas attribué de perso ahahaha sale pauvre :,)\n Allez va mendier :)")
        return render(request, "equipment/charfile.html", context={'player' : char})
    else :
        return HttpResponse('Page admin encore en construction... Fin pas commencée en vrai :,) <a href="/logout">Log out</a>')


def IndexView(request):
    if request.user.is_authenticated():
        return redirect('/charfile')
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
                    return render(request, "equipment/index.html", context={'form': form})
                return redirect('/charfile')
            else:
                return render(request, "equipment/index.html", context={'form': form})
        form = LoginForm()
        return render(request, "equipment/index.html", context={'form': form})

def LogoutView(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/')