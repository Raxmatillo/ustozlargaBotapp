from aiogram.types import Message
from data.config import ADMINS
from aiogram.dispatcher.filters import Filter



class IsAdmin(Filter):
    async def check(self, message: Message):

        return str(message.from_user.id) in ADMINS