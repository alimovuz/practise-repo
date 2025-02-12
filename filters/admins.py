from aiogram.types import Message
from aiogram.filters import BaseFilter

class IsAdminOrCreator(BaseFilter):
    async def __call__(self, message: Message):
        member = await message.chat.get_member(message.from_user.id)
        return member.status in ['creator', 'administrator']