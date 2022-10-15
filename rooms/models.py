from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

from accounts.models import Account

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = RichTextField()
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    room  = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.body