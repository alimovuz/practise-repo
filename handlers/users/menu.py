from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menu_keyboards import menu_keyboard
from aiogram import Router

menu_router = Router()

@menu_router.message(Command("menu"))
async def menu(message: Message):
    await message.answer("Kurslarni tanlang:", reply_markup=menu_keyboard)
