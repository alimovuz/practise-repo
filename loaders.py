from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from data import config
from handlers.groups.service_messages import group_router
from handlers.users.echo import echo_router

bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(group_router)
dp.include_router(echo_router)
