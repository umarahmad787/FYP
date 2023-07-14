from django import forms

class login(forms.Form):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)