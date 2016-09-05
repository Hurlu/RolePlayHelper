from django.forms import ModelForm
from django.contrib.auth import authenticate, login
from django.forms import fields

class LoginForm(ModelForm):
    login = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)

    def clear_form(self):
        user = authenticate(self.login, self.password)
        if user is None:
            raise AuthentificationError(_('Wrong credentials!'))
        else:
            login(user)