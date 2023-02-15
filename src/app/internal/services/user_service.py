import datetime
from datetime import datetime
from django.db import models

from app.internal.models.user import User


def register_user(telegram_id: int, telegram_login: str, message_date: int) -> bool:
    check_registration_result = find_user(telegram_id)

    if check_registration_result is None:
        User.objects.create(
            telegram_id=telegram_id, username=telegram_login, register_date=datetime.fromtimestamp(message_date)
        )
        return True

    return False


def find_user(telegram_id: int):
    find_user_query_result = User.objects.filter(telegram_id=telegram_id)
    if len(find_user_query_result) == 0:
        return None
    return find_user_query_result[0]


def check_registration(telegram_id: int):
    return find_user(telegram_id) is not None


def save_phone_number(telegram_id: int, phone_number: str) -> None:
    user = find_user(telegram_id)
    user.phone = phone_number
    user.save()
