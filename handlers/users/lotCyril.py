from aiogram import types
from aiogram.dispatcher import FSMContext
from handlers.users.admin import send_ad_to_all, show_statistics
from handlers.users.faq import get_user_message
from handlers.users.tarjimon import start_translate
from utils.misc import lotinKiril as lotin_kril

from states.MyState import ImloState, WikipediaState, LotinKiril, SendMessageToAdmin

from data.config import ADMINS
from utils.misc.uzwords import words

from difflib import get_close_matches

from loader import dp, bot


import wikipedia

wikipedia.set_lang("uz")



@dp.message_handler(text="📕 Wikipedia")
async def wikipediaInfo(message: types.Message):
    await message.answer("Wikipediadan qidiramiz, so'z yozing ...")
    await WikipediaState.startWikipedia.set()


@dp.message_handler(state=WikipediaState.startWikipedia)
async def wikipedia_send(message: types.Message, state: FSMContext):
    if message.text in ["/start", "/help", "📝 Xabar yuborish", "🔁 Xatosiz o'girish", "🌐 Tarjima qiling", "📌 Reklama", "📊 Statistika", '☑️Imlo-Xatoni aniqlash', '📕 Wikipedia']:
        await state.finish()
        if message.text == "📝 Xabar yuborish":
            await get_user_message(message)
        elif message.text == "🔁 Xatosiz o'girish":
            await bot_echo_lotinKiril(message)
        elif message.text == "🌐 Tarjima qiling":
            await start_translate(message)
        elif message.text == "📌 Reklama":
            await send_ad_to_all(message)
        elif message.text == "📊 Statistika":
            await show_statistics(message)
        elif message.text == 'Imlo-Xatoni aniqlash':
            await infoImlo(message)
        elif message.text == "📕 Wikipedia":
            await wikipediaInfo(message)
        else:
            await wikipediaInfo(message)
    else:
        try:
            result_word = wikipedia.summary(message.text)
            await message.answer(result_word)
        except Exception as err:
            await message.answer("Bunday ma'lumot topilmadi!")




def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False
    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ','х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    return {'available':available, 'matches':matches}

@dp.message_handler(text='☑️Imlo-Xatoni aniqlash')
async def infoImlo(message: types.Message):
    await message.answer("Tekshirish uchun so'z yuboring")
    await ImloState.startImlo.set()

@dp.message_handler(state=ImloState.startImlo)
async def checkImlo(message: types.Message, state: FSMContext):
    if message.text in ["/start", "/help", "📝 Xabar yuborish", "🔁 Xatosiz o'girish", "🌐 Tarjima qiling", "📌 Reklama", "📊 Statistika", '☑️Imlo-Xatoni aniqlash']:
        await state.finish()
        if message.text == "📝 Xabar yuborish":
            await get_user_message(message)
        elif message.text == "🔁 Xatosiz o'girish":
            await bot_echo_lotinKiril(message)
        elif message.text == "🌐 Tarjima qiling":
            await start_translate(message)
        elif message.text == "📌 Reklama":
            await send_ad_to_all(message)
        elif message.text == "📊 Statistika":
            await show_statistics(message)
        elif message.text == 'Imlo-Xatoni aniqlash':
            await infoImlo(message)
        elif message.text == "📕 Wikipedia":
            await wikipediaInfo(message)
        else:
            await infoImlo(message)
    else:
        lat_lang = False
        word = message.text
        if word[0] in lotin_kril.latin:
            print(word[0])
            lat_lang = True
            word = lotin_kril.ToCyrilic(word)

        result = checkWord(word)


        if result['available']:
            response = f'✅ {word.capitalize()}'
        else:
            response = f'❌ {word.capitalize()}\n'
            for text in result['matches']:
                response += f'✅ {text.capitalize()}\n'

        if lat_lang:
            change_word = lotin_kril.ToLatin(response)
            await message.answer(change_word)
        else:
            await message.answer(response)


@dp.message_handler(text="🔁 Xatosiz o'girish")
async def bot_echo_lotinKiril(message: types.Message):
    await message.answer("Matn kiriting ....")
    await LotinKiril.startLotinKiril.set()

@dp.message_handler(state=LotinKiril.startLotinKiril)
async def convert(message: types.Message, state: FSMContext):
    if message.text in ["/start", "/help", "📝 Xabar yuborish", "🔁 Xatosiz o'girish", "🌐 Tarjima qiling", "📌 Reklama", "📊 Statistika", '☑️Imlo-Xatoni aniqlash', '📕 Wikipedia']:
        await state.finish()
        if message.text == "📝 Xabar yuborish":
            await get_user_message(message)
        elif message.text == "🔁 Xatosiz o'girish":
            await bot_echo_lotinKiril(message)
        elif message.text == "🌐 Tarjima qiling":
            await start_translate(message)
        elif message.text == "📌 Reklama":
            await send_ad_to_all(message)
        elif message.text == "📊 Statistika":
            await show_statistics(message)
        elif message.text == 'Imlo-Xatoni aniqlash':
            await infoImlo(message)
        elif message.text == "📕 Wikipedia":
            await wikipediaInfo(message)
        else:
            await bot_echo_lotinKiril(message)
    else:
        if message.text[0] in lotin_kril.latin:
            await message.answer(lotin_kril.ToCyrilic(message.text))
        elif message.text[0] in lotin_kril.cyrilic:
            await message.answer(lotin_kril.ToLatin(message.text))
        else:
            await message.reply('Iltimos xarif bilan boshlanuvchi matn kiriting☹️')
