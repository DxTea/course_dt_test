import telebot

from app.internal.services.user_service import find_user


class Register(telebot.custom_filters.SimpleCustomFilter):
    key = "register"

    @staticmethod
    def check(message: telebot.types.Message, **kwargs):
        user = find_user(message.from_user.id)
        return user is not None


class Phone(telebot.custom_filters.SimpleCustomFilter):
    key = "phone"

    @staticmethod
    def check(message: telebot.types.Message, **kwargs):
        user = find_user(message.from_user.id)
        return user is not None and user.phone != ""
