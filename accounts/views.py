from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignUpForm, UserLoginForm, ProfilForm


# Create your views here.
def isiprofil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST)
        if form.is_valid():
            username = request.user
            isi = form.save(commit=False)
            isi.save()

        return redirect('/')
    else:
        form = ProfilForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/addprofil.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('isiprofil'))
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def loginview(request):
    # print(request.user.is_authenticated())
    # next = request.GET.get('next')
    # title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # if next:
        # 	return redirect(next)
        return redirect("/")
    context = {
        "form": form,
        # "title": title
    }

    return render(request, 'accounts/login.html', context)


def logoutview(request):
    logout(request)
    return redirect("/")
