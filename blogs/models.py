from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ..base import settings


class BlogPost(models.Model):

    # the enumeration class Status by subclassing models.TextChoices.
    # The available choices for the post status are DRAFT and PUBLISHED
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # indexes option allows you to define database indexes for your model,
    # which could comprise one or multiple fields, in ascending or descending
    # order, or functional expressions and database functions.
    # Index ordering is not supported on MySQL. If you use MySQL for the database,
    # a descending index will be created as a normal index.
    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
