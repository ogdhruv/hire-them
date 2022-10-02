from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    # we use the PasswordInput widget to render the password HTML element.
    # This will include type="password" in the HTML so
    # that the browser treats it as a password input.

    password = forms.CharField(widget=forms.PasswordInput)
