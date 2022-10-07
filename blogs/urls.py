from django.urls import path, include
from .views import BlogListView

urlpatterns = [
    path("", BlogListView.as_view(), name="blogs"),
]
