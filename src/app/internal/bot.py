import telebot
from django.conf import settings
from telebot.storage import StateMemoryStorage

from app.internal.transport.bot import handlers
from app.internal.transport.bot.handlers import filters

state_storage = StateMemoryStorage()
telegram_api = telebot.TeleBot(settings.TELEGRAM_TOKEN, state_storage=state_storage)


def run_bot():
    handlers.register_all_handlers(telegram_api)
    telegram_api.add_custom_filter(filters.Register())
    telegram_api.add_custom_filter(filters.Phone())
    telegram_api.infinity_polling()


if __name__ == "__main__":
    run_bot()
