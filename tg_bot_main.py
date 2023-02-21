"""
Здесь я прохожу курс по "ботостроению" и всячески эксперементирую
осваиваем гитхаб, не могу создать пару ключей на винде, команда ssh-keygen не работает
Место для заметок и интересностей:
- оказалось что я не правлиьно вводил команду, забыл - в команде, вывод -
====================================================================
ВСЕГДА ПРОВЕРЯЙ ТОЧНОСТЬ ВВОДА, ВСЕГДА
"""
import pprint
import requests
import datetime
from weather_api import OPEN_WEATHER_TOKEN


TOKEN = open('my_token.txt').read(46)

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


# def get_weather(city):
#     code_to_smile = {
#         'Clear': 'Ясно \U00002600',
#         'Clouds': 'Пасмурно \U00002601',
#         'Rain': 'Дождь \U00002614',
#         'Thunderstorm': 'Гроза \U000026A1',
#         'Snow': 'Снег \U0001F328',
#         'Mist': 'Туман \U0001F32B',
#     }
#     r = requests.get(
#         f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_TOKEN}&units=metric')
#     data = r.json()
#
#     time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
#     city = data['name']
#     temp = data['main']['temp']
#
#     weather_description = data['weather'][0]['main']
#     if weather_description in code_to_smile:
#         wd = code_to_smile[weather_description]
#     else:
#         wd = 'Погляди в окно сам'
#
#     pressure = data['main']['pressure']
#     feels_like = data['main']['feels_like']
#     wind = data['wind']['speed']
#     sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
#     sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
#     day_length = sunset - sunrise
#
#     return f'==== {time_now} ====\nТемпература {temp} °C {wd}\nОщущается как {feels_like} °C\n' \
#            f'Давление {pressure} мм.рт.ст\nВетер {wind} м\сек\nРассвет {sunrise}\nЗакат {sunset}\n' \
#            f'Продолжительность дня: {day_length}'
#
#
# city = input('Введите город: ')
# print(get_weather(city))


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['gg'])
async def start_bot(message: types.Message):
    await message.reply('Привет. Все запустилось.')


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Пасмурно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B',
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric')
        data = r.json()

        time_now = datetime.datetime.now().strftime('%H:%M %d-%m-%Y')
        city = data['name']
        temp = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Погляди в окно сам'

        pressure = data['main']['pressure']
        feels_like = data['main']['feels_like']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        day_length = sunset - sunrise

        await message.reply(f'Время и число: {time_now}\nТемпература {temp} °C {wd}\nОщущается как {feels_like} °C\n' \
                            f'Давление {pressure} мм.рт.ст\nВетер {wind} м\сек\nРассвет {sunrise}\nЗакат {sunset}\n' \
                            f'Продолжительность дня: {day_length}')
    except KeyError:
        await message.reply('\U00002620 Неверное название города \U00002620\n Введите город: ')


if __name__ == '__main__':
    executor.start_polling(dp)
