import logging

from aiogram.types import Message
from aiogram import Router, F
from filters import IsGroup

group_router = Router()

@group_router.message(IsGroup(), F.new_chat_members)
async def new_chat_members_messages(message: Message):
    for new_chat_member in message.new_chat_members:
        await message.answer(f"{new_chat_member.mention_html()} guruhga qo'shildi. Hello, {new_chat_member.full_name}")

@group_router.message(IsGroup(), F.left_chat_member)
async def left_chat_members_messages(message: Message):
    logging.info(message.left_chat_member)
    await message.answer(f"{message.left_chat_member.mention_html()} guruhni tark etdi! By by, {message.left_chat_member.full_name}")
