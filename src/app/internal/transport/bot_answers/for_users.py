import datetime
from telebot import types


def start_command(username: str, new_user: bool):
    if new_user:
        return f"Добро пожаловать, {username}!"
    return f"Привет, {username}!"


def me_command(username: str, telegram_id: int, phone: str,
               register_time: datetime.datetime):
    time = register_time.strftime("%m/%d/%Y, %H:%M:%S")
    return f"Ваше имя: `{username}`\nВаш Telegram id: `{telegram_id}`\nВаш номер телефона: `{phone}`\nДата регистрации: `{time}` (GMT+5)"


def markup_me(telegram_id):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("API Me",
                                        url=f'https://localhost/api/me/{telegram_id}')
    markup.add(button)


def warning_not_registered_user():
    return "Вы не зарегистрированы, введите команду /start"


def warning_unknown_message():
    return "Такой команды нет :( попробуйте /start или /me"


def set_phone_answer(valid_number):
    if valid_number:
        return "Номер телефона сохранен, чтобы изменить повторите команду"
    return "Неправильно указан телефон, введите /set_phone +7**********"
