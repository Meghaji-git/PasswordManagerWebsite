from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)

    password1 = forms.CharField(
        label="Master Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Master Password confirmation",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
