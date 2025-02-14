import telebot
from django.conf import settings
from telebot.storage import StateMemoryStorage

from app.internal.transport.bot.handlers import filters
from app.internal.transport.bot.handlers.handlers import start_message, \
    me_command, set_phone_command, warning_unknown_message

state_storage = StateMemoryStorage()
telegram_bot = telebot.TeleBot(settings.TELEGRAM_TOKEN,
                               state_storage=state_storage)


def register_all_handlers(bot):
    bot.register_message_handler(start_message, commands=["start"],
                                 pass_bot=True)
    bot.register_message_handler(me_command, commands=["me"], pass_bot=True)
    bot.register_message_handler(set_phone_command, commands=["set_phone"],
                                 pass_bot=True)
    bot.register_message_handler(warning_unknown_message,
                                 content_types=["text"], pass_bot=True)


def run_bot():
    register_all_handlers(telegram_bot)
    telegram_bot.add_custom_filter(filters.Register())
    telegram_bot.add_custom_filter(filters.Phone())
    telegram_bot.infinity_polling()


if __name__ == "__main__":
    run_bot()
