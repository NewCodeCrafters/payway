from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=12, verbose_name=_("Phone Number"), unique=True
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_owner = models.BooleanField(
        default=False,
        verbose_name=_("Owner Validity"),
        help_text=_("Designates whether User is a School Owner"),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last Login Date"), auto_now=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can has teacher's/staff's Priviledges."
        ),
    )

    verified = models.BooleanField(
        _("email verification"),
        default=False,
        help_text=_("Designates whether this user's email has been Verified. "),
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    REQUIRED_FIELDS = [
        "phone_number",
    ]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
