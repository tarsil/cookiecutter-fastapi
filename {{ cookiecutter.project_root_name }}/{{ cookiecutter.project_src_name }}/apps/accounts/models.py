from core.lib.contrib.auth.tortoise.base_user import AbstractUser


class User(AbstractUser):
    """
    Default user for the system.
    """

    class Meta:
        table = "users"

    def __str__(self):
        return self.email
