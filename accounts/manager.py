from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name, roll_no, password, department=None
    ):
        if not email:
            raise ValueError("User requires an Email")
        if not first_name:
            raise ValueError("User requires a First name")
        if not roll_no:
            raise ValueError("User requires a Roll Number")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            roll_no=roll_no,
            department=department,
            is_active=True,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, department="OT"):
        if not email:
            raise ValueError("Admin requires an Email")
        if not first_name:
            raise ValueError("Admin requires a First name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            department=department,
            is_staff=True,
            is_admin=True,
            is_superadmin=True,
            is_active=True,
            roll_number=None,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
