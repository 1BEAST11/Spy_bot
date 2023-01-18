import telebot
from cipher import *

bot = telebot.TeleBot('5878394624:AAFodenj-pdCck6WgqI6yS0S09Kjhm_GJ5U')


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот-шпион🥷! Напиши мне всё, что хочешь, а я это зашифрую.')

@bot.message_handler()
def get_user_text(message):
    phrase = message.text
    bot.send_message(message.chat.id, f"Твой шифр: {cipher(phrase)}")

bot.polling(none_stop=True)


