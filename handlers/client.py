import os
from datetime import datetime
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import WEATHER_API_TOKEN
from create_bot import bot, dp
from keybords.client_kb import kb_client
from database import sqlite_db
import requests
import json

class FSMWeather(StatesGroup):
    city = State()

# os.getenv('APITOKEN')

def parse_weather(data):
    API_TOKEN = WEATHER_API_TOKEN
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': data, 'appid': API_TOKEN, 'units': 'metric'}
    responce = requests.get(api_url, params=params)
    return responce

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добрый день, с помощью этого бота вы сможете узнать ассортимент нашего заведения, адресс, а также погоду!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напиши боту, для того стобы он мог отвечать вам в лс: \nhttps://t.me/sdt_ex_bot')

# @dp.message_handler(commands=['weather'])
async def available_city(message: types.Message):
    await FSMWeather.city.set()
    await message.reply('Введите город')

# @dp.message_handler(state=FSMWeather.city)
async def return_weather(message: types.Message, state: FSMWeather):
    if parse_weather(message.text):
        await message.answer(f'''Текущая температура в городе: {parse_weather(message.text).json()["main"]["temp"]} градуса
Скорость ветра: {parse_weather(message.text).json()["wind"]["speed"]} м/c
''')
    else:
        await message.answer('Не удалось подключиться к API погоды')
    await state.finish()

# @dp.message_handler(commands=['time'])
async def command_time(message: types.Message):
    await message.answer(datetime.now().time().strftime('%H:%M:%S'))

# @dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handler_client(dp):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(available_city, commands=['weather'])
    dp.register_message_handler(command_time, commands=['time'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(return_weather, state=FSMWeather)