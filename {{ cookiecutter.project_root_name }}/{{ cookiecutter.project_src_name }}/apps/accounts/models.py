from python_web_extras.fastapi.models.import User as AbstractUser


class User(AbstractUser):
    """
    Default user for the system.
    """

    class Meta:
        table = "users"

    def __str__(self):
        return self.email
