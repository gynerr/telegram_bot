from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/weather')
b2 = KeyboardButton('/start')
b3 = KeyboardButton('/time')
b6 = KeyboardButton('/menu')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).add(b3).add(b6)  # .row(b4, b5)
