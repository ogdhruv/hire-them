from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomRegistrationForm, CustomLoginForm


class CustomRegistrationView(CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy("login")
    redirect_authenticated_user = True
    template_name: str = "accounts/register.html"
    success_message = "You registered successfully."


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy("home")
    template_name: str = "accounts/login.html"

class CustomLogoutView(LogoutView):
    template_name: str = "accounts/logout.html"
    next_page = None