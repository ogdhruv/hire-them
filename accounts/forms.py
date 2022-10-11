from django import forms
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)

from .models import Account


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "roll_number",
            "profile_picture",
            "department",
            "bio",
        ]


class CustomLoginForm(AuthenticationForm):
    pass