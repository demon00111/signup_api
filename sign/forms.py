from django import forms

from .models import SigninForm, SignupForm

class AllData(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)
    class Meta:
        Model= SigninForm
        fields = ['username','password']

class UserData(forms.Form):
    name = forms.CharField(max_length=70)
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    class Meta:
        Model= SignupForm
        fields = ['name','username','password','email']


    
    