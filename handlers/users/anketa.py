from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from states.personal_data import PersonalData

anket_router = Router()

@anket_router.message(Command("anketa"))
async def anketa(message: types.Message, state: FSMContext):
    await message.answer("To'liq ismingizni kiriting: ")
    await state.set_state(PersonalData.full_name)

@anket_router.message(StateFilter(PersonalData.full_name))
async def process_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(PersonalData.email)
    await message.answer("Emailingizni kiriting: ")

@anket_router.message(StateFilter(PersonalData.email))
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(PersonalData.phone)
    await message.answer("Telefon raqamingizni kiriting: ")

@anket_router.message(StateFilter(PersonalData.phone))
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    full_name = data.get("full_name")
    email = data.get("email")
    phone = data.get("phone")
    await message.answer(
        f"Rahmat! Anketangiz:\n"
        f"👤 Ism: {full_name}\n"
        f"📧 Email: {email}\n"
        f"📞 Telefon: {phone}"
    )
    await state.clear()

