from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔁 Xatosiz o'girish"),
            KeyboardButton(text="🌐 Tarjima qiling"),
        ],
        [
            KeyboardButton(text="✅ Imlo-Xatoni aniqlash"),
            KeyboardButton(text="📕 Wikipedia"),
        ],
        [
            KeyboardButton(text="📝 Xabar yuborish")
        ]
    ], resize_keyboard=True
)
