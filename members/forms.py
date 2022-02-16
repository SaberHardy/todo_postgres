from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your username here'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your email here'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Type your password here'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Type your confirmation password here'

        # self.fields['password1'].help_text = None

        for field_name in ['username', 'password1', 'password2']:  # or self.fields
            self.fields[field_name].help_text = None


class UpdateProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your username here'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your email here'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your first name here'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your last name here'}))

    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(widget=forms.TextInput(attrs=
    #                                                      {'class': 'form-control',
    #                                                       'placeholder': 'Date joined'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'is_superuser', 'is_active', 'is_staff')

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].widget.attrs['placeholder'] = 'User name'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['placeholder'] = 'Type your password here'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Type your confirmation password here'

        # self.fields['password1'].help_text = None

        for field_name in self.fields:
            self.fields[field_name].help_text = None


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your old password'}))

    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your new password'}))

    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your confirmation password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
