from django.urls import path
from .views import CustomLogoutView, CustomRegistrationView, CustomLoginView

urlpatterns = [
    path("register/", CustomRegistrationView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/",CustomLogoutView.as_view(),name="logout"),
]
