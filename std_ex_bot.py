import os

from aiogram import types
from aiogram.utils import executor
from sqlalchemy import URL

from create_bot import dp
from database import sqlite_db, create_async_eng, get_session_maker, proceed_schemas, BaseModel
from handlers import client, other, admin
from dotenv import load_dotenv

load_dotenv()

async def on_startup(_):
    print('Бот вышел в онлайн')
    postgres_url = URL.create('postgresql+asyncpg', username=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), \
                              database=os.getenv('DB_NAME'), port=os.getenv('DB_PORT'))
    async_engine = create_async_eng(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)
    # await sqlite_db.sql_start()


client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
