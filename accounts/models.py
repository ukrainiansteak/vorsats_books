from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, image, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            image=image,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name="", last_name="", phone_number=None, image=None):
        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            image=image,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Profile(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        unique=True
    )
    phone_number = models.CharField(
        null=True,
        max_length=24,
        validators=[
            RegexValidator(r'^(\+?\d\d?)?\d{10}$',
                           message="Phone should be in format +381112223344")
        ])
    image = models.ImageField(
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png'])
        ]
    )

    objects = UserManager()
