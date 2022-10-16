from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

from accounts.models import Account  #!TODO change
from jobs.models import Company  #!TODO change


class Room(models.Model):
    host = models.ForeignKey(Account, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = RichTextField()
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
