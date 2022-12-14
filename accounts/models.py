from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# AbstractUser can also be used because it already have some predefined model fields
# and we can add more if we want to.
class Account(AbstractBaseUser):
    # choices for departement
    class Department(models.TextChoices):
        CSE = "CSE", "COMPUTER SCIENCE"
        IT = "IT", "INFORMATION TECHNOLOGY"
        EE = "EE", "ELECTRIC ENGINEERING"
        CE = "CE", "CIVIL ENGINEERING"
        TE = "TE", "TEXTILE ENGINEERING"
        ME = "ME", "MECHANICAL ENGINEERING"
        OT = "OT", "OTHER"

    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.PositiveIntegerField(unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="photos/profiles", blank=True)
    bio = models.TextField(null=True, blank=True)

    department = models.CharField(
        max_length=30,
        choices=Department.choices,
        blank=True,
        null=True,
    )

    # required
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    def __str__(self) -> str:
        if self.roll_number and self.first_name:
            return "{} - {}".format(self.email, self.roll_number)

        else:
            return self.email

    # must add in
    def get_profile_image_filename(self):
        return str(self.profile_picture)[
            str(self.profile_picture).index(f"photos/profiles/{self.pk}/")
        ]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
