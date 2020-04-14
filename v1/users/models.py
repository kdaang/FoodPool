from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import upper


class UserManager(BaseUserManager):
    def create_user(self, email, user_type, first_name, last_name, password, **extra_fields):
        email = self.normalize_email(email)
        first_name = upper(first_name)
        last_name = upper(last_name)

        user = self.model(email=email, user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_type='ADMIN', first_name='admin', last_name='admin', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    user_id = models.BigAutoField(primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    user_type = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []