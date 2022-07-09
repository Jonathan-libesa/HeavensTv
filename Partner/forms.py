from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import*
from Users.models import*
from django.forms import ModelForm
from Main.validators import validate_file_size,file_size

class PartnerSignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','phone','country','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_partner = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        partner= Partner.objects.create(user=user)
        partner.save()
        return user


class UserForm(ModelForm):
    profile_pic=forms.ImageField(required=True,validators=[file_size])
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','phone','profile_pic','country','Occupation']


class DonateForm(forms.ModelForm):
    class Meta:
        model=Donate
        fields='__all__'


class ContributeForm(forms.ModelForm):
    class Meta:
        model=Contribute
        fields='__all__'
        exclude =['partner']