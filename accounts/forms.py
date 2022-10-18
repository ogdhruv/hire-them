from django import forms
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from .models import Account


class CustomRegistrationForm(UserCreationForm):
    # DEPARTMENT_CHOICES = [
    #     ("CSE", "COMPUTER SCIENCE"),
    #     ("IT", "INFORMATION TECHNOLOGY"),
    #     ("EE", "ELECTRIC ENGINEERING"),
    #     ("CE", "CIVIL ENGINEERING"),
    #     ("TE", "TEXTILE ENGINEERING"),
    #     ("ME", "MECHANICAL ENGINEERING"),
    #     ("OT", "OTHER"),
    # ]
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "id": "Email",
                "name": "email",
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "id": "FirstName",
                "name": "first_name",
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "id": "LastName",
                "name": "last_name",
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
                "type": "password",
                "id": "Password1",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
                "type": "password",
                "id": "Password2",
                "placeholder": "Password",
            }
        ),
    )

    roll_number = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "id": "RollNumber",
                "name": "roll_number",
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
            }
        ),
    )

    # department = forms.ChoiceField(
    #     choices=DEPARTMENT_CHOICES
    # )

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                "cols": 50,
                "class": "mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm",
            }
        )
    )

    class Meta:
        model = Account
        fields = "__all__"


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-500 bg-white border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 focus:border-blue-400 focus:border-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Email Address",
                "type": "email",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "block w-full px-4 py-2 mt-2 text-gray-700 placeholder-gray-500 bg-white border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 focus:border-blue-400 focus:border-blue-300 focus:ring-opacity-40 focus:outline-none focus:ring focus:ring-blue-300",
                "type": "password",
                "placeholder": "Password",
            }
        ),
    )
