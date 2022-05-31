# SubmitBand_bot
# Author: Mohammed Mahdi Ali

import telebot
import os
from time import sleep
import submit
import threading

BOT_TOKEN = '5572083536:AAEHek4j8y6Mut-FkM5bhzurx5j_e20rQuY'
bot = telebot.TeleBot(BOT_TOKEN)
bot_users = [i.strip('\n') for i in open('users.txt','r').readlines()]
admin_id = '834403140'

welcome_message = '''مرحبا بك في بوت تقديم الطعن للحسابات المعطلة\n
للتقديم يرجى تحضير المتطلبات التالية (بللغة الانكيزية):\n
الاسم الكامل\n
اسم المستخدم\n
الاميل\n
رقم الهاتف\n
الرسالة\n
الوقت الفاصل بين كل طلب (ساعة)\n
مع فصل كل المتطلبات ب ~'''

contact = 'www.facebook.com/admail123'

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
	sent = bot.send_message(message.chat.id, welcome_message)

@bot.message_handler(commands=['submit'])
def go(message):
	to_check_id = str(message.chat.id)
	if to_check_id in bot_users or to_check_id == admin_id:
		sent = bot.send_message(message.chat.id, 'ادخل المعلومات بلترتيب')
		bot.register_next_step_handler(sent, requirements_handler)
	else:
		bot.send_message(message.chat.id, f'لا يمكن للمستخدم {message.chat.id} استخدام البوت يرجى التواصل مع {contact}')

def requirements_handler(message):

	data = []

	if '/' in message.text:
		bot.send_message(message.chat.id, 'ادخل الامر مره اخرى')

	else:
		try:
			for d in message.text.split('#'):
				data.append(d)
		except:
			bot.send_message(message.chat.id, 'يرجى اعادة التقديم و التحقق من المعلومات')

		try:
			done_message = 'تم تشغيل السكربت, و سوف تتم عملية التقديم بشكل مستمر و اذا كان المستخدم محضور سوف تتم تكرار العملية بعد الوقت المحدد منك'

			t = threading.Thread(target=submit.submit,args=(data[0], data[1], data[2], data[3], data[4], data[5]))
			t.daemon = True
			t.start()

			bot.send_message(message.chat.id, done_message)

		except:
			bot.send_message(message.chat.id, 'حدث خطا في عملية تشغيل السكربت, يرجى تكرار المحاولة لاحقا')

@bot.message_handler(commands=['add'])
def add(message):
	sent = bot.send_message(message.chat.id, 'ادخل رقم المستخدم الجديد')
	bot.register_next_step_handler(sent, add_user)
	
def add_user(message):
	if '/' in message.text:
		bot.send_message(message.chat.id, 'ادخل الامر مره اخرى')
	else:
		try:
			if str(message.chat.id) == admin_id:
				bot_users.append(str(message.text))
				with open('users.txt','a+') as f:
					f.write('\n'+str(message.text))
				bot.send_message(message.chat.id, 'تم اضافة المستخدم')
			else:
				bot.send_message(message.chat.id, 'لا يمكنك اضافة مستخدم جديد. تحقق من رقم المستخدم او من صلاحياتك')
		except:
			bot.send_message(message.chat.id, 'لا يمكنك اضافة مستخدم جديد. تحقق من رقم المستخدم او من صلاحياتك')

@bot.message_handler(commands=['delete'])
def delete(message):
	sent = bot.send_message(message.chat.id, 'ادخل رقم المستخدم للحذف')
	bot.register_next_step_handler(sent, delete_user)

def delete_user(message):
	if '/' in message.text:
		bot.send_message(message.chat.id, 'ادخل الامر مره اخرى')
	else:
		try:
			if str(message.chat.id) == admin_id:
				bot_users.remove(str(message.text))
				with open('users.txt', 'w') as f:
					for user in bot_users:
						if not user.startswith(str(message.text)):
							f.write(user)

				bot.send_message(message.chat.id, 'تم حذف المستخدم')
			else:
				bot.send_message(message.chat.id, 'لا يمكنك حذف المستخدم. تحقق من رقم المستخدم او من صلاحياتك')
		except:
			bot.send_message(message.chat.id, 'لا يمكنك حذف المستخدم. تحقق من رقم المستخدم او من صلاحياتك')

while True:
	try:
		bot.polling(none_stop = True)
	except Exception as e:
		sleep(2)