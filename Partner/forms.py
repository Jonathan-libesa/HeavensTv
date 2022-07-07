from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import*
from Users.models import*
from django.forms import ModelForm
from Main.validators import validate_file_size,file_size

class PartnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['first_name','last_name','email','country','phone','Occupation','password1','password2']

class UserForm(ModelForm):
    profile_pic=forms.ImageField(required=True,validators=[file_size])
    class Meta:
        model = User
        fields = '__all__'


class DonateForm(forms.ModelForm):
    class Meta:
        model=Donate
        fields='__all__'


