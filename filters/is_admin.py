from aiogram.types import Message
from data.config import ADMINS
from aiogram.dispatcher.filters import Filter



class IsAdmin(Filter):
    async def check(self, message: Message):
        print(type(message.from_user.id))
        print(type(ADMINS))
        print(f"{message.from_user.id} in {ADMINS}")
        print(message.from_user.id in ADMINS)
        return str(message.from_user.id) in ADMINS