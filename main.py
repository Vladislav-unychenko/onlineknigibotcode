import telebot
import sqlite3
from telebot import types

from config import TOKEN
from config import db
from config import admin

import functionals as func
import keyboard as kb
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
	
	user_id = message.chat.id
	connection = sqlite3.connect(db)
	q = connection.cursor()
	q = q.execute('SELECT * FROM users WHERE user_id IS '+str(user_id))
	row = q.fetchone()
	if row is None:
		invaite = 0
		count_list_book = 0,10
		func.first_join(user_id=message.chat.id, username=message.chat.username, invaite=invaite, count_list_book_kd=count_list_book)
	
		message_start_user = 'Привет помогу найти книгу)'

		bot.send_message(message.chat.id,message_start_user,parse_mode='html',reply_markup=kb.glav_menu)
		connection.close()
	else:
		glav_menu = ('Главное меню')
		bot.send_message(message.chat.id, glav_menu,parse_mode='html',reply_markup=kb.glav_menu)
		connection.close()

# Функция админа
@bot.message_handler(commands=['admin'])
def start_admin(message: types.Message):
	if message.chat.id == admin:
		bot.send_message(message.chat.id, ' {}, вы авторизованы!'.format(message.from_user.first_name),reply_markup=kb.admin)




@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.message:
		#>>> Переменные для функции админ
		chat_id = call.message.chat.id
		message_id = call.message.message_id
		#>>> После кнопки продолжить 
		
		if call.data == 'list':
			keyboard_list_books = types.InlineKeyboardMarkup(row_width=2)
			list_books = func.check_all_book(func.cheack_list_books_users(chat_id))

			for i in range(0, len(list_books)):
				keyboard_list_books.add(types.InlineKeyboardButton(text=f'{func.check_all_book(func.cheack_list_books_users(chat_id))[i]}', callback_data=f"{i}"))

			keyboard_list_books.add(
				types.InlineKeyboardButton(text='<<<', callback_data='beek'),
				types.InlineKeyboardButton(text='>>>', callback_data='next')
				)
			message_text_list_books_kd = 'Все книги которые доступны:'
			
			try:
				bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text_list_books_kd, parse_mode='html',reply_markup=keyboard_list_books)
			except Exception as ex:
				pass



		if call.data == 'search':
			message_text_search = 'Напишите название книги:'
			send = bot.send_message(call.message.chat.id, message_text_search, parse_mode='html')
			bot.register_next_step_handler(send,func.check_books_users)

		if call.data == 'courses':
			pass
		
		if call.data == 'info':
			pass

		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
		# # # # # # # # # # # # # # # # # # # # # CPISOK-KNIR-OBRABOTKA-KNOPOK# # # # # # # # # # # # # # # # # # # # # # # # # 
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

		if call.data == '0':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[0]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '1':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[1]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '2':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[2]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '3':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[3]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '4':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[4]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)	

		if call.data == '5':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[5]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '6':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[6]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '7':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[7]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)

		if call.data == '8':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[8]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)	

		if call.data == '9':
			name_books = func.check_all_book(func.cheack_list_books_users(chat_id))[9]

			print(func.check_books_adres(name_books))
			document = open(func.check_books_adres(name_books), "rb")
			bot.send_document(call.message.chat.id, document)	

		if call.data == 'next':
			func.update_count_list_num_user(chat_id,1)
			
			list_books = func.check_all_book(func.cheack_list_books_users(chat_id))

			keyboard_list_books1 = types.InlineKeyboardMarkup(row_width=2)
			for i in range(0, len(list_books)):
				keyboard_list_books1.add(types.InlineKeyboardButton(text=f'{func.check_all_book(func.cheack_list_books_users(chat_id))[i]}', callback_data=f"{i}"))

			keyboard_list_books1.add(
				types.InlineKeyboardButton(text='<<<', callback_data='beck'),
				types.InlineKeyboardButton(text='>>>', callback_data='next')
				)
			message_text_list_books_kd = 'Все книги которые доступны:'
			
			# try:
			bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text_list_books_kd, parse_mode='html',reply_markup=keyboard_list_books1)
			# except Exception as ex:
			# 	pass

		if call.data == 'beck':
			func.update_count_list_num_user(chat_id,0)
			list_books = func.check_all_book(func.cheack_list_books_users(chat_id))

			keyboard_list_books2 = types.InlineKeyboardMarkup(row_width=2)
			
			for i in range(0, len(list_books)):
				keyboard_list_books2.add(types.InlineKeyboardButton(text=f'{func.check_all_book(func.cheack_list_books_users(chat_id))[i]}', callback_data=f"{i}"))

			keyboard_list_books2.add(
				types.InlineKeyboardButton(text='<<<', callback_data='beck'),
				types.InlineKeyboardButton(text='>>>', callback_data='next')
				)
			message_text_list_books_kd = 'Все книги которые доступны:'
			
			# try:
			bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text_list_books_kd, parse_mode='html',reply_markup=keyboard_list_books2)
			# except Exception as ex:
				# pass




		if call.data == 'reload_books':
			message = '<b>Кидайте файл для обновления:</b>'
			send = bot.send_message(call.message.chat.id, message, parse_mode='html')
			bot.register_next_step_handler(send,func.update_books_name)




if __name__ == '__main__':
	bot.polling()	