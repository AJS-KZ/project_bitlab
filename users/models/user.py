from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractUUID, AbstractTimeTracker
from users.managers import CustomUserManager
from utils.const import GenderChoice


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    phone = models.CharField(
        max_length=13,
        verbose_name='phone',
        unique=True
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name='first_name'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='last_name'
    )
    avatar = models.ImageField(
        upload_to='uploads/avatars/',
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=70,
        blank=True,
        null=True,
        unique=True,
        verbose_name='email'
    )
    gender = models.CharField(
        choices=GenderChoice.choice(),
        max_length=6,
        blank=True,
        null=True,
        verbose_name=_('gender')
    )
    is_staff = models.BooleanField(
        default=True
    )
    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('uuid', )

    def __str__(self):
        return str(self.phone)
