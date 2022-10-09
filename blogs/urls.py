from django.urls import path, include
from .views import( BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView,BlogCreateView)

urlpatterns = [
    path("", BlogListView.as_view(), name="blogs"),
    path("post/newblog/",BlogCreateView.as_view(),name="blog_create"),
    path("post/<int:pk>/",BlogDetailView.as_view(),name="blog_detail"),
    path("post/<int:pk>/udpate",BlogUpdateView.as_view(),name="blog_update"),
    path("post/<int:pk>/delete",BlogDeleteView.as_view(),name="blog_delete"),

]
