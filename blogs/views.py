from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name: str = "blogs/blog_create.html"
    fields = ["title", "author", "body"]


class BlogListView(ListView):
    model = Post
    template_name: str = "blogs/blogs_home.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Post
    template_name: str = "blogs/blog_detail.html"
    context_object_name: str = "blog"


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name: str = "blogs/blog_update.html"
    context_object_name: str = "blog"
    fields = ["title", "body"]


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name: str = "blogs/blog_delete.html"
    success_url = "blogs"
