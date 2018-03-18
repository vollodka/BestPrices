import telebot
from telebot import types
from collections import namedtuple
from settings import TOKEN
import requests

import datetime

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Порівняти ціну на один товар'))
    markup.add(types.KeyboardButton('Порівняти ціну на корзину'))
    # markup.add(types.KeyboardButton('Оборот по магазинам'))
    bot.send_message(message.chat.id, "Оберіть Опцію.", reply_markup=markup)


@bot.message_handler(func=lambda message: 'Порівняти ціну на один товар' == message.text)
def top_products(message):
    bot.send_message(message.chat.id, "Загрузіть фото штрих коду")
    bot.register_next_step_handler(message, handle_file)
    # file_get_contents("https://api.telegram.org/bot$apiToken/sendMessage?".http_build_query($data) );
    # bot.send_message()


@bot.message_handler(func=lambda message: 'Порівняти ціну на корзину' == message.text)
def compare_basket(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Завантажити')
    markup.row('Стоп')
    bot.send_message(message.chat.id, "Загрузіть фото штрих коду", reply_markup=markup)
    bot.register_next_step_handler(message, handle_next_photo_uploading)
    # file_get_contents("https://api.telegram.org/bot$apiToken/sendMessage?".http_build_query($data) );
    # bot.send_message()


def handle_file(message):
    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))

        with open('imgs/out.png', 'wb') as f:
            f.write(file.content)


def handle_next_photo_uploading(message):
    if message.text and message.text.lower() == 'стоп':
        func(message)
        return

    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))

        with open('out.png', 'wb') as f:
            f.write(file.content)

    markup = types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, "Загрузіть фото штрих коду", reply_markup=markup)
    bot.register_next_step_handler(message, handle_next_photo_uploading)


def func(message):
    bot.send_message(message.chat.id, "Result")

#@bot.message_handler(func=lambda message: 'Оборот по магазинам' == message.text)
#def turnover_by_shops(message):



bot.polling()
