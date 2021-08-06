from django import forms
from .models import person, detail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2" , )



class PersonForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ("name", "phone", "dob", "gender"
                 )


class DetailForm(forms.ModelForm):
    class Meta:
        model = detail
        fields = ( "height", "weight" , "active" )

