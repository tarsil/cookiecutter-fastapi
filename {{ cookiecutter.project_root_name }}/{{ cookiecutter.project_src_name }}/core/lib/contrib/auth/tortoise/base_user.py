from multiprocessing.dummy import Manager

from tortoise import fields
from tortoise.models import Model

from ..hashers import check_password, is_password_usable, make_password


class PermissionsMixin(Model):
    """
    Add the fields and methods necessary to support the Group and Permission
    models using the ModelBackend.
    """

    is_superuser = fields.BooleanField(default=False)

    class Meta:
        abstract = True


class AbstractUser(PermissionsMixin, Model):
    """
    Base model used for a custom model of an application.
    contains
    """

    first_name = fields.CharField(description="First name", max_length=150, unique=True)
    last_name_name = fields.CharField(
        description="Last name", max_length=150, unique=True
    )
    username = fields.CharField(description="Username", max_length=150, unique=True)
    email = fields.CharField(description="Email address", max_length=120)
    password = fields.CharField(description="Password", max_length=128)
    last_login = fields.DatetimeField(description="Last login", null=True)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)

    # Stores the raw password if set_password() is called so that it can
    # be passed to password_changed() after the model is saved.
    _password = None

    class Meta:
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

    @classmethod
    def _create_user(cls, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        user = cls(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    @classmethod
    def create_user(cls, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return cls._create_user(username, email, password, **extra_fields)

    @classmethod
    def create_superuser(cls, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return cls._create_user(username, email, password, **extra_fields)
