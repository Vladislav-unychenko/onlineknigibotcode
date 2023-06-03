import telebot
import requests
import sqlite3
import os
from config import db, TOKEN

bot = telebot.TeleBot(TOKEN)
#>>> Запись пользователей в базу данных
def first_join(user_id,username,invaite,count_list_book_kd):
    connection = sqlite3.connect(db)
    q = connection.cursor()
    q = q.execute('SELECT * FROM users WHERE user_id IS '+str(user_id))
    row = q.fetchone()
    if row is None:
        q.execute("INSERT INTO users (user_id,nick,invaite,count_list_book_kd) VALUES ('%s', '%s', '%s', '%s')"%(user_id,username,invaite,count_list_book_kd))
        connection.commit()
    connection.close()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-+-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>> Рассылка админ для пользователей
def admin_message(text):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f'SELECT user_id FROM users')
    row = cursor.fetchall()
    return row
    conn.close()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-+-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>> Статистика пользователей через админ панель
def stats():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT user_id FROM users').fetchone()
    amount_user_all = 0
    while row is not None:
        amount_user_all += 1
        row = cursor.fetchone()
    msg = '❕ Информация:\n\n❕ Пользователей в боте - ' + str(amount_user_all)
    return msg
    conn.close()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-+-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 


def check_books_users(message):
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
	books = cursor.execute(f"SELECT name_book FROM books").fetchone()
	count_column = 0
	while books is not None:
		if str(books[0]).lower() == str(message.text).lower():
			books_adres = cursor.execute(f"SELECT adres_book FROM books").fetchall()
			book_one_list = books_adres[count_column]
			# return(book_one_list[0])
			document = open(book_one_list[0], "rb")
			bot.send_document(message.chat.id, document)
			break
		count_column += 1
		books = cursor.fetchone()
	connect.close()



def check_all_book(count_list):
	books_list_count = count_list.split(':')
	one_count_num = int(books_list_count[0])
	too_count_num = int(books_list_count[1])
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
	books = cursor.execute(f"SELECT name_book FROM books").fetchone()
	book_list = []
	while books is not None:
		book_list.append(books[0])
		books = cursor.fetchone()
	connect.close()
	return(book_list[one_count_num:too_count_num])


def test_check_books(num_one,num_too):
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
	books = cursor.execute(f"SELECT name_book FROM books").fetchone()
	book_list = []
	count_column = 0
	while books is not None:
		count_column += 1
		if count_column >= num_one:
			book_list.append(books[0])
			if count_column == num_too:
				break
		books = cursor.fetchone()
	connect.close()
	return(book_list)



# print(test_check_books(5,6))


def cheack_list_books_users(message_id):
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
    # Определение user_id 
	user_id = cursor.execute(f"SELECT user_id FROM users").fetchone()
	count_column = 0
	while user_id is not None:
        # User_id в строку
		user_id_str = str(user_id[0])
        # Определение если user_id то далее
		if user_id_str == str(message_id):
			user_list_user = cursor.execute(f"SELECT count_list_book_kd FROM users").fetchall()
			user_list_int = user_list_user[count_column]

			str_user_list = str(user_list_int[0])
			step_1 = str_user_list.replace('(','')
			step_2 = step_1.replace(')','')
			step_3 = step_2.replace(',',':')
			step_4 = step_3.replace(' ','')
			return(step_4)
			break

		count_column += 1
		user_id = cursor.fetchone()

	connect.close()
# print(cheack_list_books_users(716837984))
def update_count_list_num_user(message_id, move):
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
	# Определение user_id 
	user_id = cursor.execute(f"SELECT user_id FROM users").fetchone()
	count_column = 0
	list_user_count = 0
	while user_id is not None:
        # User_id в строку
		user_id_str = str(user_id[0])
		count_column += 1
        # Определение если user_id то далее
		
		if user_id_str == str(message_id):
			user_list_user = cursor.execute(f"SELECT count_list_book_kd FROM users").fetchall()
			user_list_int = user_list_user[list_user_count]
			str_user_list = str(user_list_int[0])

			step_1 = str_user_list.replace('(','')
			step_2 = step_1.replace(')','')
			step_3 = step_2.replace(',','')
			step_4 = step_3.split(' ')

			if move == 1:
				
				step_5 = int(step_4[1]) + 10
				step_6_go = f'({step_4[1]}, {step_5})'

				if count_column > 0:
					cursor.execute(f"UPDATE users SET count_list_book_kd = '{step_6_go}' WHERE rowid = {count_column}")
					connect.commit()
				if count_column == 0:
					cursor.execute(f"UPDATE users SET count_list_book_kd = '{step_6_go}' WHERE rowid = 1")
					connect.commit()
				break

			if move == 0:
				step_5 = int(step_4[1]) - 10
				step_6_go = f'({step_5 - 10}, {step_5})'
				if step_5 - 10 >= 0:
					if count_column > 0:
						cursor.execute(f"UPDATE users SET count_list_book_kd = '{step_6_go}' WHERE rowid = {count_column}")
						connect.commit()
					if count_column == 0:
						cursor.execute(f"UPDATE users SET count_list_book_kd = '{step_6_go}' WHERE rowid = 1")
						connect.commit()
					break
				else:
					pass

			break

		list_user_count += 1
		user_id = cursor.fetchone()

	connect.close()

def reload_name_boks_sql(name_book,adres_book):
	connection = sqlite3.connect(db)
	q = connection.cursor()
	# q = q.execute("SELECT * FROM books WHERE name_book IS "+str(name_book))

	# # IS '+str(name_book))
	# row = q.fetchone()
	# print(row)
	# if row is None:
	q.execute("INSERT INTO books VALUES ('%s', '%s')"%(name_book, adres_book))
	connection.commit()
	connection.close()

	# else:
	# 	print('non')
	# connection.close()
# Поиск по названию книги и выдача её адреса (пути)
def check_books_adres(name_books):
	connect = sqlite3.connect(db)
	cursor = connect.cursor()
	books = cursor.execute(f"SELECT name_book FROM books").fetchone()
	count_column = 0
	while books is not None:
		if str(books[0]).lower() == str(name_books).lower():
			books_adres = cursor.execute(f"SELECT adres_book FROM books").fetchall()
			book_one_list = books_adres[count_column]
			return(book_one_list[0])
			# document = open(book_one_list[0], "rb")
			# bot.send_document(message.chat.id, document)
			break
		count_column += 1
		books = cursor.fetchone()
	connect.close()


def update_books_name(message):
	chat_id = message.chat.id

	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	name_file = str(message.document.file_name.partition(".")[0])
    
	src = 'Books/' + message.document.file_name;
	with open(src, 'wb') as new_file:
		new_file.write(downloaded_file) 

	name_book_and_file = f'{name_file}.pdf'
	name_adres_books = f'Books/{name_book_and_file}'
	reload_name_boks_sql(name_book_and_file,name_adres_books)
	bot.reply_to(message, " Сохранено✅ ")
















# def update_count_list_books():
# 	connect = sqlite3.connect(db)
#     cursor = connect.cursor()
#     user_id = cursor.execute(f"SELECT facultet_name FROM name_file_raspisanie").fetchone()
#     count_column = 0

    
#     while user_id is not None:
#         user_id_str = str(user_id[0])
#         count_column += 1
#         if user_id_str == str(facultet):
#             if count_column > 0:
#                 cursor.execute(f"UPDATE name_file_raspisanie SET adres_file = '{link}' WHERE rowid = {count_column}")
#                 connect.commit()
                
#             if count_column == 0:
#                 cursor.execute(f"UPDATE name_file_raspisanie SET adres_file = '{link}' WHERE rowid = 1")
#                 connect.commit()
                
#             break

#         user_id = cursor.fetchone()

#     connect.close()











# def baza():
#     db = sqlite3.connect('baza_books_bot.db')
#     sql = db.cursor()

#     sql.execute("""CREATE TABLE IF NOT EXISTS users(
#         user_id  TEXT,
#         nick TEXT,
#         invaite BIGINT,
#         count_list_book_kd BIGINT
#     )""")
#     sql.execute("""CREATE TABLE IF NOT EXISTS books(
#     	name_book TEXT,
#     	adres_book TEXT
#     )""")

#     db.commit()

