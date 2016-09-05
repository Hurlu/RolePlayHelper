from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def IndexView(request):
    if request.user:
        pass
    else:
        #login
        pass
    return HttpResponse("Wai euh là c'est pas fini frère, rajoute /admin à ton url plzplz")