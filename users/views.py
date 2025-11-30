import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import Profile

logger = logging.getLogger(__name__)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            user_exists = get_user_model().objects.get(email=data['email'])

            user = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                logger.info('Попытка логина')
                login(request, user)
                messages.success(request, 'login successfully', 'success')
                return redirect('main:home')
            else:
                logger.info('Ошибка логина')
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully', 'success')
    return redirect('main:home')


def register(request):
    if request.method == 'POST':
        logger.info("register::POST")

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            logger.info(f"Password {form.cleaned_data['password']}")

            new_user.set_password(form.cleaned_data['password'])

            new_user.save()

            Profile.objects.create(user=new_user)

            # Автоматический вход после регистрации
            from django.contrib.auth import login
            login(request, new_user)
            return redirect('main:home')  # Редирект на главную вместо render
    else:
        logger.info("register::GET")
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})
