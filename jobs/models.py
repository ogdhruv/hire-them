from django.db import models
from django.urls import reverse
from accounts.models import Account  #!TODO change
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# Create your models here.
class Company(models.Model):
    # class JobType(models.TextChoices):
    #     INTERNSHIP = 'IS', _('INTERNSHIP')
    #     FULLTIME = 'FT', _('FULLTIME')
    #     PARTTIME = 'PT', _('PARTTIME')

    name = models.CharField(max_length=200)
    type = models.TextChoices("JobType", "INTERN FULLTIME PARTTIME")
    # type = models.CharField(max_length=2,choices=JobType.choices,default=JobType.FULLTIME)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comapany"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    postedby = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tag = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})
