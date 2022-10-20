import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, name, tel, password, **extra_fields):
        user = self.model(tel=tel, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, tel, name, password=None, **extra_fields):
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(tel, name, password, **extra_fields)

    def create_superuser(self, tel, name, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(tel, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tel = models.CharField(
        min_length=8,
        max_length=8,
        unique=True,
        validators=[RegexValidator(regex=r"^\d{8}$", message="Must be 8 digits")],
    )
    name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=False, db_index=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = "tel"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        constraints = [
            models.UniqueConstraint(name="unique_active_tel", fields=["tel"], condition=models.Q(is_active=True)),
        ]

    def __str__(self):
        return f"{self.name} ({self.tel})"
