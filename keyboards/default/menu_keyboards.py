from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text="C#"),
            KeyboardButton(text="C++"),
            KeyboardButton(text="JavaScript")
         ]
    ], resize_keyboard=True
)