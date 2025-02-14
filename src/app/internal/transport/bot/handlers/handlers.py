import telebot
from phonenumber_field.validators import to_python

from app.internal.transport.bot_answers import for_users as users_answers
from app.internal.services.user_service import register_user_and_return_status, \
    save_phone_number, find_user

import logging

logger = logging.getLogger(__name__)


def start_message(message: telebot.types.Message, bot: telebot.TeleBot):
    logger.info(
        (message.from_user.id, message.from_user.full_name, message.date))
    new_user = register_user_and_return_status(message.from_user.id,
                                               message.from_user.full_name,
                                               message.date)
    text = users_answers.start_command(message.from_user.full_name, new_user)
    bot.send_message(message.from_user.id, text)


def me_command(message: telebot.types.Message, bot: telebot.TeleBot):
    user = find_user(message.from_user.id)
    if user is None:
        text = users_answers.warning_not_registered_user()
    else:
        text = users_answers.me_command(user.username, user.telegram_id,
                                        user.phone, user.register_date)
    bot.send_message(message.from_user.id, text, parse_mode="markdown")


def set_phone_command(message: telebot.types.Message, bot: telebot.TeleBot):
    args = message.text.split()[1:]
    try:
        valid_number = len(args) > 0 and to_python(args[0]).is_valid()
    except:
        valid_number = False

    text = users_answers.set_phone_answer(valid_number)

    if valid_number:
        save_phone_number(message.from_user.id, args[0])

    bot.send_message(message.from_user.id, text)


def warning_unknown_message(message: telebot.types.Message,
                            bot: telebot.TeleBot):
    bot.send_message(message.from_user.id,
                     users_answers.warning_unknown_message())
