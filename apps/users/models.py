from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    AbstractUser
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Метод создания обычного пользователя."""
        if not email:
            raise ValueError("Необходимо указать адрес электронной почты")
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Метод создания суперпользователя."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Суперпользователь должен иметь is_superuser=True."
            )
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя. Идентификатор - поле email."""

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField("Активный", default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        constraints = [
            models.UniqueConstraint(
                fields=['email', 'password'],
                name='unique_user'
            )
        ]

    def __str__(self):
        return self.email
