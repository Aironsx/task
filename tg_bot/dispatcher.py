import asyncio
import logging

from aiogram import Bot, Dispatcher

from Task.settings import BOT_TOKEN
from tg_bot.handlers import notification

logger = logging.getLogger(__name__)


def register_handlers(dp):
    """
    Register handlers
    """
    notification.register_handlers(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    register_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


def cli():
    """Wrapper for command line"""
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")


if __name__ == '__main__':
    cli()
