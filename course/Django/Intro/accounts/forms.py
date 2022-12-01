from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
