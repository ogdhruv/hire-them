from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name: str = "blogs/blogs_home.html"
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Post
    template_name: str = "blogs/blog_detail.html"
    context_object_name: str = "blog"

class BlogUpdateView(UpdateView):
    model = Post
    template_name: str = "blogs/blog_update.html"
    context_object_name: str = "blog"
    fields = ["title","slug","body"]