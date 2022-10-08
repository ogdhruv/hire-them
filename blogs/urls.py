from django.urls import path, include
from .views import BlogDetailView, BlogListView, BlogUpdateView

urlpatterns = [
    path("", BlogListView.as_view(), name="blogs"),
    path("post/<int:pk>/",BlogDetailView.as_view(),name="blog_detail"),
    path("post/<int:pk>/udpate",BlogUpdateView.as_view(),name="blog_update"),

]
