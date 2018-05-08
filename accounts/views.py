from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)
from .forms import SignUpForm, UserLoginForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'accounts/signup.html', {'form':form})

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