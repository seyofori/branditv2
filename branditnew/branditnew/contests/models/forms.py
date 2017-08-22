from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .contest import Contest
from . import skills




class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput()
    )
    # skills = forms.ModelChoiceField(
    #     queryset=skills.objects.all()
    # )
    birth_date = forms.DateField(
        help_text='Required. Format: YYYY-MM-DD'
    )


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', ]


class CreateContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = [
            'client', 
            'title', 
            'about', 
            'prize', 
            'end_date', 
            'is_top', 
            'is_hidden', 
            'is_nda', 
            'is_sealed', 
            'cost', 
            'files',
        ]