import logging

from aiogram import Router
from aiogram.types import Message

from filters import IsAdminOrCreator
from filters import IsGroup

echo_router = Router()

@echo_router.message(IsGroup())
async def echo(message: Message):
    await message.answer(message.text)