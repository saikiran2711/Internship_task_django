from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthForm
from django.contrib.auth.models import User


# from  .models import Profile


def register(request):
    rform = RegisterForm()
    if request.method == "POST":
        rform = RegisterForm(request.POST)
        try:
            User.objects.get_by_natural_key(
                username=request.POST.get('username'))
            messages.error(request, "User with this user name already exists!!")
            print("in try last")
        except User.DoesNotExist:
            if rform.is_valid():
                rform.save()
                print("user saved to database")
                return redirect('login')
    return render(request, 'accounts/register.html', {'rform': rform,})


@login_required()
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def home(request):
    username = request.user.username
    return render(request, 'accounts/home.html', {'username': username})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            username = User.objects.get(username = username)
        except User.DoesNotExist:
            messages.error(request, "User Not found !")
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User Not found !")
            return redirect('login')
    return render(request, "accounts/login.html", {'form': form,})


def index(request):
    return render(request, 'accounts/index.html')
