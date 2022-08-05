from multiprocessing.dummy import Manager

from django.contrib.auth.models import User
from tortoise import fields
from tortoise.models import Model

from ..hashers import check_password, is_password_usable, make_password
from .manager import UserManager


class PermissionsMixin(Model):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """

    is_superuser = fields.BooleanField(default=False)

    class Meta:
        abstract = True


class AbstractUserModel(PermissionsMixin, Model):
    """
    Base model used for a custom model of an application.
    contains
    """

    username = fields.CharField(description="Username", max_length=150, unique=True)
    email = fields.CharField(description="Email address")
    password = fields.CharField(description="Password", max_length=128)
    last_login = fields.DateTimeField(description="Last login", null=True)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)

    # Stores the raw password if set_password() is called so that it can
    # be passed to password_changed() after the model is saved.
    _password = None

    class Meta:
        manager = UserManager()
        abstract = True

    async def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            # password_validation.password_changed(self._password, self)
            self._password = None

    # from django.contrib.auth import get_user_model

    @property
    def is_authenticated(self):
        """
        Always return True.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
        self.save()

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.password)
