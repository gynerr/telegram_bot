import os
from config import API_KEY
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
# os.getenv('TOKEN') для переменной среды окружения

bot = Bot(token=API_KEY)
dp = Dispatcher(bot, storage=storage)

