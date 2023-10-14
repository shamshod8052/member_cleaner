from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return types.ChatType.PRIVATE == message.chat.type
