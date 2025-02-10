from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from data import config
from handlers.users.anketa import anket_router
from handlers.users.menu import menu_router

bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(anket_router)
dp.include_router(menu_router)
