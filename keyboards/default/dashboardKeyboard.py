from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📌 Reklama"),
            KeyboardButton(text="📊 Statistika")
        ]
    ], resize_keyboard=True
)