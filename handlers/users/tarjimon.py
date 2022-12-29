from aiogram import types
from aiogram.dispatcher import FSMContext
from states.MyState import Translate
from aiogram.dispatcher.filters import Command
from googletrans import Translator

from loader import dp

translator = Translator()

@dp.message_handler(text="🌐 Tarjima qiling")
async def start_translate(message: types.Message):
    text = ("<b>❗️ Tarjima qilish uchun Qo'llanma! 📝</b>\n",
            "Inglizchaga tarjima qilish uchun -- <b>/en</b> <i>so'z</i>",
            "Ruschaga tarjima qilish uchun -- <b>/ru</b> <i>so'z</i>",
            "O'zbekchaga tarjima qilish uchun -- <b>/uz</b> <i>so'z</i>\n\n"
            "Misol uchun:  /uz apple")

    await message.answer("\n".join(text))
    # await Translate.startTranslate.set()

@dp.message_handler(Command("en", prefixes="!/"))
async def to_eng(message: types.Message):
    # if message.text == "/lotinkiril":
    #     await state.finish()
    # else:
    uz = message.text[4:]

    eng = translator.translate(uz, src='auto', dest="en")
    word = eng.text
    await message.reply(f"{word}")
    print(message.text)
    print(word)

@dp.message_handler(Command("ru", prefixes="!/"))
async def to_eng(message: types.Message):
    
    
    
    uz = message.text[4:]

    eng = translator.translate(uz, src='auto', dest="ru")
    word = eng.text
    await message.reply(f"{word}")
    print(message.text)
    print(word)

@dp.message_handler(Command("uz", prefixes="!/"))
async def to_eng(message: types.Message):
    
    
    
    uz = message.text[4:]

    eng = translator.translate(uz, src='auto', dest="uz")
    word = eng.text
    await message.reply(f"{word}")
    print(message.text)
    print(word)




#
# uz = message.text
#
# 	eng = translator.translate(uz, src='auto', dest="en")
# 	word = eng.text
# 	await message.reply(f"{word}")
# 	print(message.text)
# 	print(word)