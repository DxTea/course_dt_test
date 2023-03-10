# Generated by Django 4.2a1 on 2023-02-14 20:39

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("telegram_id", models.IntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=120)),
                ("phone", phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ("register_date", models.DateTimeField()),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
