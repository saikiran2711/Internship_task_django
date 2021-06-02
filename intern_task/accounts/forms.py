from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):

    def clean_username(self):
        print("Entering here")
        username = self.cleaned_data['username']
        if not ((username[0] =='a' or username[0] == 'A')  and  (username[len(username) - 1] == '0'  or username[len(username) - 1] == '1')):
            print("Not valid username")
            raise  ValidationError("Username must begin with a/A and end with 0/1")
        return username
    class Meta:
        model = User
        fields = ['username',  'date_joined', 'password1', 'password2']





class AuthForm(forms.Form):
    username = forms.CharField(required= True)
    password = forms.PasswordInput()

