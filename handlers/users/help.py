from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(
        "<b>- Bot orqali hariflarni lotindan kirilga va kirildan lotinga oson o'giring\n</b>"
        "<b>- O'zbek/Rus/Ingliz tillarida so'zlarni tarjima qiling\n\n</b>"
        "<i>Agar shikoyat va takliflar bo'lsa bizga yuboring, albatta ko'rib chiqamiz!</i>"
        )