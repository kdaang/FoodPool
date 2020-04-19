from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import upper
from phonenumber_field.modelfields import PhoneNumberField

from v1.core.models import TimestampedModel


class UserTypes:
    GRABBER = 'GRABBER'
    ORDERER = 'ORDERER'
    ADMIN = 'ADMIN'

    choices = [
        (GRABBER, 'GRABBER'),
        (ORDERER, 'ORDERER'),
        (ADMIN, 'ADMIN')
    ]


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, user_type, first_name, last_name, password):
        email = self.normalize_email(email)
        first_name = upper(first_name)
        last_name = upper(last_name)

        user = self.model(email=email, phone_number=phone_number, user_type=user_type, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, phone_number, password, user_type=UserTypes.ADMIN, first_name='admin', last_name='admin'):
        user = self.create_user(email=email, phone_number=phone_number, user_type=user_type, first_name=first_name,
                                last_name=last_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    objects = UserManager()

    email = models.EmailField(db_index=True, unique=True)
    phone_number = PhoneNumberField(db_index=True, unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    user_type = models.CharField(max_length=256, choices=UserTypes.choices)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['phone_number']
