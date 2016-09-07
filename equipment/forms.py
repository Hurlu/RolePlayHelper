from django.forms import Form
from django.contrib.auth import authenticate, login
from django.forms import fields
from django.forms.widgets import PasswordInput

class LoginForm(Form):
    login = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100, widget=PasswordInput())
