from aiogram import types 
from aiogram.dispatcher import FSMContext
from states.MyState import LotinKiril, SendMessageToAdmin
from utils.misc import lotinKiril as lotin_kril
from data.config import ADMINS
from loader import dp, bot



@dp.message_handler(text="📝 Xabar yuborish")
async def get_user_message(message: types.Message):
    await message.answer("❗️ <i>Shikoyat/taklif matnini kiriting ...</i>")
    await SendMessageToAdmin.message.set()


@dp.message_handler(state=SendMessageToAdmin.message, content_types="text")
async def send_to_admin(message: types.Message, state: FSMContext):
    await message.answer("ℹ️ Tashakkur! Xabaringiz adminga yuborildi")
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=message.text, disable_web_page_preview=True)
    await state.finish()

@dp.message_handler(state=SendMessageToAdmin.message, content_types=["photo", "video", "audio", "file"])
async def unknown_command(message: types.Message):
    await message.answer("Iltimos, matn ko'rinishida yuboring !")