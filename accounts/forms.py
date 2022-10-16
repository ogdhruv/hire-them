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
    username = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-500 bg-white border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 focus:border-blue-400 focus:border-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Email Address",
                "type": "email"
            }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
        attrs={
            "class":"block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-500 bg-white border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 focus:border-blue-400 focus:border-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-blue-300", 
            "type":"password", 
            "placeholder":"Password"
        }),
    )