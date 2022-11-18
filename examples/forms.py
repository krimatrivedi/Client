from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Book,Project
from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
   
)

class BookFilterForm(BSModalForm):
    type = forms.ChoiceField(choices=Book.BOOK_TYPES)

    class Meta:
        fields = ['type']
class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class BookModelForm(BSModalModelForm):
   

    class Meta:
        model = Book
        exclude = ['timestamp']
attendance_choices = (
    ('absent', 'Afwezig'),
    ('allowedabsent', 'Geoorloofd afwezig'),
    ('present', 'Aanwezig'),
)

def field_style():
     styles_string = ' '

     # List of what you want to add to style the field
     styles_list = [
            'width: 10% !important;',
           'align-items: center;',
          
            'height: 10px !important;',
            
     ]
    # Converting the list to a string 
     styles_string = styles_string.join(styles_list)
     # or
     # styles_string = ' '.join(styles_list)
     return styles_string

class ProjectModelForm(BSModalModelForm):
   

    class Meta:
        model = Project
        widgets = (
            {'gender': forms.RadioSelect(attrs={'style': field_style()})})
   
        exclude = ['timestamp']


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
