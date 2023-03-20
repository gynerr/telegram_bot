from aiogram import types
from aiogram.utils import executor
from create_bot import dp
from database import sqlite_db
from handlers import client, other, admin


async def on_startup(_):
    print('Бот вышел в онлайн')
    await sqlite_db.sql_start()


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
