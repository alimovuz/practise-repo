from aiogram.types import Message
from aiogram.filters import BaseFilter

class IsGroup(BaseFilter):
    async def __call__(self, message: Message):
        return message.chat.type in ['group', 'supergroup']