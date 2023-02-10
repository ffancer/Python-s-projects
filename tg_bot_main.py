"""
Здесь я прохожу курс по "ботостроению" и всячески эксперементирую
осваиваем гитхаб, не могу создать пару ключей на винде, команда ssh-keygen не работает
Место для заметок и интересностей:
- оказалось что я не правлиьно вводил команду, забыл - в команде, вывод -
====================================================================
ВСЕГДА ПРОВЕРЯЙ ТОЧНОСТЬ ВВОДА, ВСЕГДА
"""
TOKEN = open('my_token.txt').read(46)

from typing import Union, List, Optional, Literal, Any

# в пайчарме разницы нет, указывать тип данных или нет, но это яляется хорошей практикой написания кода
# def say_something(number: int, word: str) -> str:
# #     word = word.capitalize()
# #     return word * number
# #
# #
# # def test(number_1: int, number_2: int, word='well done') -> tuple:
# #     return number_1 * number_2, word
# #
# #
# # print(test(4, 5))


# from dataclasses import dataclass
#
#
# @dataclass
# class DatabaseConfig:
#     db_host: str       # URL-адрес базы данных
#     db_user: str       # Username пользователя базы данных
#     db_password: str   # Пароль к базе данных
#     database: str      # Название базы данных
#
#
# @dataclass
# class TgBot:
#     token: str             # Токен для доступа к телеграм-боту
#     admin_ids: list[int]   # Список id администраторов бота
#
#
# @dataclass
# class Config:
#     tg_bot: TgBot
#     db: DatabaseConfig
#
#
# config = Config(tg_bot=TgBot(token=BOT_TOKEN,
#                              admin_ids=ADMIN_IDS),
#                 db=DatabaseConfig(db_host=DB_HOST,
#                                   db_user=DB_USER,
#                                   db_password=DB_PASSWORD,
#                                   database=DATABASE))


# def get_string(string: str, number: int) -> str:
#     return string * number
#
#
# print(get_string.__annotations__)


# где прямо сейчас находится Международная Космическая Станция.
# import requests
#
# api_url = 'http://api.open-notify.org/iss-now.json'
#
# response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
#
# if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#     print(response.text)
# else:
#     print(response.status_code)    # При другом коде ответа выводим этот код


# import requests
#
# api_url = 'http://numbersapi.com/' + '43'
# res = requests.get(api_url).text
#
# try:
#     print(res)
# except:
#     print(res.status_code)


# import random
# import requests
# import time
#
#
# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = '*'
# # TEXT: str = 'Привет Паша :*'
# # TEXT: str = random.choice(['a', 'b', 'c', 'd'])
# MAX_COUNTER: int = 20
#
# offset: int = -2
# counter: int = 0
# chat_id: int
#
#
# while counter < MAX_COUNTER:
#
#     print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
#
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             # requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
#             requests.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={random.choice(['Котик', 'Зая', ':*', 'Малыш'])}")
#
#     time.sleep(1)
#     counter += 1


# import requests
# import time
#
#
# API_URL: str = 'https://api.telegram.org/bot'
# API_CATS_URL: str = 'https://aws.random.cat/meow'
# BOT_TOKEN: str = '*'
# ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
#
# offset: int = -2
# counter: int = 0
# cat_response: requests.Response
# cat_link: str
#
#
# while counter < 15:
#     print('attempt =', counter)
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()['file']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
#
#     time.sleep(1)
#     counter += 1


# import requests
# import time
#
#
# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = TOKEN
# offset: int = -2
# updates: dict
#
#
# def do_something() -> None:
#     print('Был апдейт')
#
#
# while True:
#     start_time = time.time()
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             do_something()
#
#     time.sleep(3)
#     end_time = time.time()
#     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


# import requests
# import time


# API_URL: str = 'https://api.telegram.org/bot'
# BOT_TOKEN: str = TOKEN
# offset: int = -2
# timeout: int = 60
# updates: dict
#
#
# def do_something() -> None:
#     print('Был апдейт')
#
#
# while True:
#     start_time = time.time()
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
#
#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             do_something()
#
#     end_time = time.time()
#     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет!\nНапиши мне что-нибудь!")
#
#
# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
#
#
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#
#
# @dp.message_handler(content_types=['photo'])
# async def get_file_id_p(message: types.Message):
#     # await message.reply(message.photo[-1].file_id)
#     await message.reply_photo(message.photo[-1].file_id)
#
#
# @dp.message_handler(content_types=['voice'])
# async def get_file_id_p(message: types.Message):
#     await message.reply_voice(message.voice.file_id)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)


# from telebot import types

import telebot
import random
import config


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    rnumber = random.randint(0, 100)
    bot.send_message(message.chat.id, 'Отгадайте число от 0 до 100, у вас 5 попыток')
    bot.register_next_step_handler(message, get_number, 1, rnumber)


def get_number(message: types.Message, try_num: int, right_num: int):
    if message.text.isdigit():
        if right_num == int(message.text):
            bot.send_message(message.chat.id, 'Вы отгадали число!')
        else:
            if try_num >= 4:
                bot.send_message(message.chat.id, 'Мимо! Попытки кончились!')
                return

            if right_num < int(message.text):
                bot.send_message(message.chat.id, 'Загаданное число меньше введенного.')
            else:
                bot.send_message(message.chat.id, 'Загаданное число больше введенного.')
            bot.register_next_step_handler(message, get_number, try_num + 1, right_num)

    else:
        bot.send_message(message.chat.id, 'Вы ввели не число. Попробуйте еще раз.')
        bot.register_next_step_handler(message, get_number, try_num, right_num)