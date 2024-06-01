import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def create_reply_markup(buttons: list) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    key_buttons = []
    for button in buttons:
        key_buttons.append(KeyboardButton(text=button))
    markup.add(key_buttons)
    return markup
