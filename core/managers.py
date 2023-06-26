from django.contrib.auth.models import BaseUserManager


class CustomBaseManager (BaseUserManager):
    def _create_user(self,email, password, **extra_fields):

        if not email:
            raise ValueError("An Email must be provided")

        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        

        user.set_password(password)

        user.save(using = self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


