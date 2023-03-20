import json
import string
from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):
    with open('mat_json.json', encoding='Utf-8') as f:
        ban_words = set(json.load(f))
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}.intersection(
            ban_words):
        await message.reply('Маты запрещены')
        await message.delete()
    elif message.text == 'Привет':
        await message.answer('И тебе привет!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
