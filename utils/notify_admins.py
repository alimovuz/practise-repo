import logging
from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

from data.config import ADMINS


async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi!")
        except TelegramAPIError as err:
            logging.exception(f"Telegram API error: {err}")
        except Exception as err:
            logging.exception(f"Xatolik yuz berdi: {err}")
