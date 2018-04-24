from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from accounts.forms import SignUpForm
from django.contrib.auth import get_user_model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signedup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signedup(request):
    return render(request,'signedup.html')

def my_account(request):
    return render(request,'my_account.html')

def password_changed(request):
    return render(request,'password_changed.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_changed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


# Create your views here.
