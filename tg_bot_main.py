"""
Здесь я прохожу курс по "ботостроению" и всячески эксперементирую
осваиваем гитхаб, не могу создать пару ключей на винде, команда ssh-keygen не работает
Место для заметок и интересностей:
- оказалось что я не правлиьно вводил команду, забыл - в команде, вывод -
====================================================================
ВСЕГДА ПРОВЕРЯЙ ТОЧНОСТЬ ВВОДА, ВСЕГДА
"""
import requests
import datetime
from weather_api import OPEN_WEATHER_TOKEN
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = open('my_token.txt').read(46)
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['gg'])
async def start_bot(message: types.Message):
    await message.reply('Привет. Все запустилось.')


@dp.message_handler(commands=['курс'])
async def start_bot(message: types.Message):
    try:
        url = 'http://www.finmarket.ru/currency/rates/'
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        all_money = soup.find_all('div', class_='value')
        dollar = all_money[0].text
        euro = all_money[1].text
        await message.reply(f'Привет. Курс валют следующий:\nДоллар - {dollar}\nЕвро - {euro}')
    except:
        await message.reply('Что-то пошло не так.')


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

        await message.reply(f'Дата {time_now:^15}\nТемпература {temp} °C {wd}\nОщущается как {feels_like} °C\n' \
                            f'Давление {pressure} мм.рт.ст\nВетер {wind} м\сек\nРассвет {sunrise}\nЗакат {sunset}\n' \
                            f'Продолжительность дня {day_length}')
    except KeyError:
        await message.reply('\U00002620 Неверное название города \U00002620\n Введите город: ')


if __name__ == '__main__':
    executor.start_polling(dp)
