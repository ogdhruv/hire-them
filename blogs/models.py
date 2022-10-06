from django.db import models
from ..accounts.models import Account


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
