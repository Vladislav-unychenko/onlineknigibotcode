import sqlite3
from telebot import types

glav_menu = types.InlineKeyboardMarkup(row_width=2)
glav_menu.add(
	types.InlineKeyboardButton(text='Список книг',callback_data='list'),
	types.InlineKeyboardButton(text='Поиск книг',callback_data='search')
	)
glav_menu.add(
	types.InlineKeyboardButton(text='Курсы', callback_data='courses')
	)
glav_menu.add(
	types.InlineKeyboardButton(text='Информация', callback_data='info')
	)

admin = types.InlineKeyboardMarkup(row_width=2)
admin.add(
    types.InlineKeyboardButton(text = 'Рассылка',callback_data='message'),
    types.InlineKeyboardButton(text = 'Статистика', callback_data='statistics')
    )
admin.add(
    types.InlineKeyboardButton(text = 'Отправка одному', callback_data='onesend')
    )
admin.add(
	types.InlineKeyboardButton(text = 'Добавить книгу', callback_data='reload_books')
	)
# keyboard_list_books = types.InlineKeyboardMarkup(row_width=2)
# keyboard_list_books.add(
# 	types.InlineKeyboardButton(text=f'{message.chat.id}',callback_data='111')
# 	)
# keyboard_list_books.add(
# 	types.InlineKeyboardButton(text='<<<', callback_data='beek'),
# 	types.InlineKeyboardButton(text='>>>', callback_data='next')
# 	)