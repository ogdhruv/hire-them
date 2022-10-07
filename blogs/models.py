from django.db import models
from django.urls import reverse
from accounts.models import Account


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
