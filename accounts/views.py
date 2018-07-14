from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

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
            if request.POST.get("methods"):
                g = Group.objects.get(name='methodsvids') 
                g.user_set.add(user)
                user.save()
            if request.POST.get("physics"):
                g = Group.objects.get(name='physicsvids') 
                g.user_set.add(user)
                user.save()
            login(request, user)
            return redirect('my_account')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def my_account(request):
    return render(request,'my_account.html')

def password_changed(request):
    return render(request,'password_changed.html')

@login_required
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
