import telebot
import logging
from telebot.types import Message
from constants import BOT_TOKEN, LOGS_PATH
from units import *

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=LOGS_PATH,
    filemode="w"
)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_hendler(message: Message):

    bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}!\n"
                                           f"Я - бот, который как и озвучивает текст, так и расшифровывает аудио.\n"
                                           f"Используй '/help' при возникновении ошибок.")
    bot.send_message(message.from_user.id, "Присылай текст или аудио:", reply_markup=create_reply_markup(["Начать!"]))

@bot.message_handler(func=lambda message: message.type == 'text')
def text_to_voice(message: Message):



if __name__ == "__main__":
    logging.info("бот запущен")
    print("бот запущен")
