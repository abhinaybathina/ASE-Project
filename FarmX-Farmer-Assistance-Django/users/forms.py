from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from farm.models import state_choices, crop_choices, Farm


class RegistrationForm(UserCreationForm):
    ROLES = [('Farmers', 'Farmers'), ('Staff', 'Staff')]
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example : Ravi Varma'}), label='Name')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Example : ravi@gmail.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example : RaviVarma15'}))
    role = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2', 'role']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'village', 'image']


# class FarmQueryForm(forms.Form):
#     state = forms.ChoiceField(label='State', choices=state_choices, required=False)
#     village = forms.CharField(label='Village/City', max_length=100, required=False)
#     crop = forms.ChoiceField(label='Crop', choices=crop_choices, required=False)

class VillageQueryForm(forms.Form):
    village = forms.CharField(label='Village/City', max_length=100)


class StateQueryForm(forms.Form):
    state = forms.ChoiceField(label='State', choices=state_choices)


class CropQueryForm(forms.Form):
    crop = forms.ChoiceField(label='Crop', choices=crop_choices)
