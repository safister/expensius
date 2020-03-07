from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .models import Account

from .forms import UserLoginForm, UserRegisterForm, AccountForm

# Create your views here.
def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        if next:
            return redirect(next)
        return redirect('/')
    
    context = {
        'forms':form
    }
    return render(request, 'expensius/login.html',context)

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        user = form.save(commit = False)
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password = password)
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        if next:
            return redirect(next)
        return redirect('account/')
    
    context = {
        'forms':form
    }
    return render(request, 'expensius/register.html',context)

@login_required
def account_info(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        user = request.user
        accnt_name = form.cleaned_data.get('accountname')
        available_bal = form.cleaned_data.get('current_bal')
        Account.objects.create(username=user, account_name=accnt_name, available_bal=available_bal)

        return redirect('/')

    context = {
        'forms':form
    }
    return render(request, 'expensius/fillaccnt.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')