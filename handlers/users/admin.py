import asyncio
from filters import IsAdmin
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.dashboardKeyboard import admin_keyboards, cancel_keyboard

from data.config import ADMINS
from states.AdminState import ReklamaState
from loader import dp, db, bot

@dp.message_handler(IsAdmin(), state="*", text="🚫 Bekor qilish")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Bekir qilindi", reply_markup=admin_keyboards)

@dp.message_handler(IsAdmin(), text="/admin")
async def admin_panel(message: types.Message):
    await message.answer("Siz adminpaneldasiz!", reply_markup=admin_keyboards)

@dp.message_handler(IsAdmin(), text="📌 Reklama")
async def send_ad_to_all(message: types.Message):
    await message.answer("Menga reklamani yuboring ...", reply=cancel_keyboard)
    await ReklamaState.reklama.set()


@dp.message_handler(IsAdmin(), state=ReklamaState.reklama, content_types=['text', 'photo', 'video', 'audio', 'file'])
async def send_reklama(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        if message.photo:
            await bot.send_photo(chat_id=user_id, photo=message.photo[-1].file_id, caption=message.caption)
        elif message.video:
            await bot.send_video(chat_id=user_id, video=message.video.file_id, caption=message.caption)
        else:
            try:
                await bot.send_message(chat_id=user_id, text=message.text, disable_web_page_preview=True)
            except Exception as e:
                print(e)
        await asyncio.sleep(0.05)
    await message.answer("Reklama yuborildi !")
    await state.finish()


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")

@dp.message_handler(IsAdmin(), text="📊 Statistika")
async def show_statistics(message: types.Message):
    count = db.count_users()
    await message.answer(f"<b>Botda foydalanuvchilar soni: {count[0]} ta</b>")