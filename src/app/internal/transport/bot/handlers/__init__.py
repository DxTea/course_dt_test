import telebot

from app.internal.transport.bot.handlers import handlers

def register_all_handlers(bot: telebot.TeleBot):
    bot.register_message_handler(handlers.start_message, commands=["start"], pass_bot=True)
    bot.register_message_handler(handlers.set_phone_command, register=True, commands=["set_phone"], pass_bot=True)
    bot.register_message_handler(handlers.me_command, register=True, phone=True, commands=["me"], pass_bot=True)
    bot.register_message_handler(handlers.warning_unknown_message, pass_bot=True)
