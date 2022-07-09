from aiogram import types
from aiogram.types import KeyboardButton


def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
            KeyboardButton('get_data')
    ]
    keyboard.add(*buttons)
    return keyboard
