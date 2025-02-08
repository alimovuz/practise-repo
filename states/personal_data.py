from aiogram.filters.state import StatesGroup, State
class PersonalData(StatesGroup):
    full_name = State()
    email = State()
    phone = State()