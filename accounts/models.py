from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    #    choice field for student department to which he belongs to
    #    add more if you want to this is just for Engineering students
    #    please change department max_length according to your max_length available.
    class Department(models.TextChoices):
        CSE = "COMPUTER SCIENCE ENGINEERING"
        EE = "ELECTRICAL ENGINEERING"
        TE = "TEXTILE ENGINEERING"
        ME = "MECHANICAL ENGINEERING"
        IT = "INFORMATION TECHNOLOGY"
        OT = "OTHER"

    roll_number = models.PositiveBigIntegerField(unique=True)
    departement = models.CharField(
        max_length=30, choices=Department.choices, default=Department.OT
    )

    class Meta:
        ordering = ["roll_number"]
