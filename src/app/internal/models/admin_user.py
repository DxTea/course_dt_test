from django.contrib.auth.models import AbstractUser


class AdminUser(AbstractUser):
    pass

    class Meta:
        verbose_name = "Admin User"
        verbose_name_plural = "Admin Users"
