from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput,TextInput,PasswordInput


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

        widgets={
            "email":EmailInput(attrs={"placeholder":"Work Email","required":True}),
            "first_name":TextInput(attrs={"placeholder":"First name","required":True}),
            "last_name":TextInput(attrs={"placeholder":"Last name","required":True}),
            "username":TextInput(attrs={"placeholder":"Username","required":True}),
            "password":PasswordInput(attrs={"placeholder":"Password","required":True}),
        }
