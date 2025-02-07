import asyncio
import logging
import sys

from loaders import dp, bot
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup():
    await set_default_commands(bot)
    await on_startup_notify(bot)


async def main():
    await on_startup()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())