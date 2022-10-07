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
