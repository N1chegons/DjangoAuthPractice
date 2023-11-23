from django.contrib.auth import authenticate, login

from UnisApp.models import Profile

from .forms import LoginForm, UserRegistrationForm, EditProfileForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'main.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main.html')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'username or password not correct')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        else:
            messages.error(request, 'Please check if all the fields are filled in correctly')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {'form': form})

def profiles(request):
    context = {
        'form': request.user,
    }
    return render(request, 'user-account.html', context)


