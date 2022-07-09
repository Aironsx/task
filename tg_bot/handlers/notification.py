from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tg_bot.handlers.keyboard import start_keyboard
from tg_bot.handlers.static_text import start_page_text, send_notification_text
from tg_bot.tasks import get_notification_data


async def start_page(message: types.Message):
    keyboard = start_keyboard()
    await message.answer(
        start_page_text,
        reply_markup=keyboard
    )


async def send_notification(message: types.Message):
    """
    Function send all task data
    """
    await message.answer(send_notification_text)
    data = await get_notification_data()
    # Получить дату и отправить, либо если токен устрале выдать форму для
    # ввода нового пароля и логина для получения нового токена


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_page, commands='start')
    dp.register_message_handler(send_notification, Text(equals='get_data'))
