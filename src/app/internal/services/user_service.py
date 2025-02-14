from datetime import datetime
from django.utils import timezone

from django.db import models
from app.internal.models.user import User


def register_user_and_return_status(telegram_id: int, telegram_login: str,
                                    message_date: int) -> bool:
    user, created = User.objects.update_or_create(
        telegram_id=telegram_id,
        defaults={
            'username': telegram_login,
            'register_date': timezone.make_aware(
                datetime.fromtimestamp(message_date))
        }
    )
    return created


def find_user(telegram_id: int):
    user = User.objects.filter(telegram_id=telegram_id).first()
    return user


def check_registration(telegram_id: int):
    return find_user(telegram_id) is not None


def save_phone_number(telegram_id: int, phone_number: str) -> None:
    user = find_user(telegram_id)
    user.phone = phone_number
    user.save()
