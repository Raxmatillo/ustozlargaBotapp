from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Amalni bajaring yoki quyidagi tugmalardan birini tanlang 👇")
