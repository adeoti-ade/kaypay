from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from kaypay.utils.base_models import BaseModel

from .managers import UserManager


class User(AbstractBaseUser, BaseModel):
    """
    This is a custom user model that inherits the abstract base user and safe delete mode
    """

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.python manage.py migrate

    objects = UserManager()

    @property
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    @property
    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.staff

    @property
    def is_admin(self):
        """Is the user a admin member?"""
        return self.admin

    @property
    def is_active(self):
        """Is the user active?"""
        return self.active

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"id": self.id})


# class User(AbstractUser):
#     """Default user for kaypay."""
#
#     #: First and last name do not cover name patterns around the globe
#     name = CharField(_("Name of User"), blank=True, max_length=255)
#     first_name = None  # type: ignore
#     last_name = None  # type: ignore
#
#     def get_absolute_url(self):
#         """Get url for user's detail view.
#
#         Returns:
#             str: URL for user detail.
#
#         """
#         return reverse("users:detail", kwargs={"username": self.username})
