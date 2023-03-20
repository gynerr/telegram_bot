from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import dp

url_kd = InlineKeyboardMarkup(row_width=1)
url_b1 = InlineKeyboardButton(text='Ссылка', url='https://youtube.com')
url_b2 = InlineKeyboardButton(text='Ссылка2', url='https://google.com')

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Доступные ссылка', reply_markup=url_kd)