from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class SupplierManager(BaseUserManager):
    def create_user(self, passport, password, **extra_fields):
        """
        Создаёт и возвращает пользователя с указанным email и паролем.
        """
        if not passport:
            raise ValueError("The passport field must be set")
        user = self.model(passport=passport, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, passport, password, **extra_fields):
        """
        Создаёт и возвращает суперпользователя.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(passport, password, **extra_fields)


class Supplier(AbstractBaseUser):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    password = models.CharField(verbose_name="password", max_length=128, null=True, blank=True)
    passport = models.CharField(max_length=20, verbose_name="Паспорт")
    experience = models.PositiveIntegerField(verbose_name="Стаж")
    delivered_goods_count = models.PositiveIntegerField(default=0, verbose_name="Количество доставленных товаров")
    balance = models.FloatField(default=0.0, verbose_name="Баланс")
    photo = models.ImageField(upload_to="suppliers/photos/", null=True, blank=True, verbose_name="Фото")
    is_staff = models.BooleanField(default=False, verbose_name="Персонал")

    objects = SupplierManager()

    USERNAME_FIELD = "passport"  # Поле для аутентификации
    REQUIRED_FIELDS = ["full_name", "password"]

    class Meta:
        verbose_name = "Грузчик"
        verbose_name_plural = "Грузчики"

    def __str__(self):
        return self.full_name
