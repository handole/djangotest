from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model ()


class SignUpForm (UserCreationForm):
    email = forms.CharField (max_length=254, required=True, widget=forms.EmailInput ())
    password1 = forms.CharField (widget=forms.PasswordInput)
    password2 = forms.CharField (widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get ('email')

        email_qs = User.objects.filter (email=email)
        if email_qs.exists ():
            raise forms.ValidationError ("This email has already been registered")

        return super (UserRegisterForm, self).clean (*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get ('password1')
        password2 = self.cleaned_data.get ('password2')
        if password1 != password2:
            raise forms.ValidationError ("Password must be match")


class UserLoginForm (forms.Form):
    username = forms.CharField ()
    password = forms.CharField (widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get ("username")
        password = self.cleaned_data.get ("password")
        # user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate (username=username, password=password)
            if not user:
                raise forms.ValidationError ("This user does not exist")
            if not user.check_password (password):
                raise forms.ValidationError ("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError ("This user is not longer active")
        return super (UserLoginForm, self).clean (*args, **kwargs)


class ProfilForm (forms.ModelForm):
    class Meta:
        model = Profil
        field = (
            'firstname',
            'lastname',
            'username',
            'email',
            'gender',
            'location',
            'bio',
        )
