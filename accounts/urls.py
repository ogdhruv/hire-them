from django.urls import path
from .views import CustomRegistrationView, CustomLoginView

urlpatterns = [
    path("signUp", CustomRegistrationView.as_view(), name="signup"),
    path("logIn", CustomLoginView.as_view(), name="login"),
]
