import phonenumber_field.modelfields
from django.db import models


class User(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, null=True)
    phone = phonenumber_field.modelfields.PhoneNumberField(blank=True)
    register_date = models.DateTimeField()

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = "Bot User"
        verbose_name_plural = "Bot Users"
