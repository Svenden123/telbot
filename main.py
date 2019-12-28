import telebot
import time
from config import TG_API_URL

bot = telebot.TeleBot('972451719:AAFyH4T_Xj4ek0q7fMRbWHE-sX4EQjtcXQk')
base_url = TG_API_URL

@bot.message_handler(commands=['start'])


def letsgo(message):
	key=telebot.types.InlineKeyboardMarkup()
	b1=telebot.types.InlineKeyboardButton(text="Яблоки", callback_data="0")
	b2=telebot.types.InlineKeyboardButton(text="Груши", callback_data="1")
	b3=telebot.types.InlineKeyboardButton(text="Поддержка",url="https://t.me/svendq")
	key.add(b1, b2)
	key.add(b3)
	bot.send_message(message.chat.id, "Привет 🍪"+message.from_user.first_name+"🍪")
	bot.send_message(message.chat.id, "Ваш текст. Я отвечу в течении 12 часов если надо👩🏻🔧", reply_markup=key)
	bot.send_chat_action(message.chat.id, action='typing')
	bot.send_chat_action(message.chat.id, action='typing')
@bot.message_handler(commands=['help'])
def helper(message):
	bot.send_message(message.chat.id, "Помогу чем смогу")
@bot.callback_query_handler(func=lambda c:True)
def prnt(c):
	bot.send_chat_action(c.message.chat.id, action='typing')
	if c.data=="0":
		bot.send_message(c.message.chat.id, "Здесь нечто про яблоки")
	elif c.data=="1":
		bot.send_message(c.message.chat.id, "Здесь про груши")
@bot.message_handler(content_types=["text"])
def ii(message):
	key=telebot.types.InlineKeyboardMarkup()
	b1=telebot.types.InlineKeyboardButton(text="Яблоки", callback_data="0")
	b2=telebot.types.InlineKeyboardButton(text="Груши", callback_data="1")
	b3=telebot.types.InlineKeyboardButton(text="Поддержка",url="https://t.me/svendq")
	key.add(b1, b2)
	key.add(b3)
	if message.text == "привет":
		bot.send_message(message.chat.id, "Здравствуй.\nНужна помощь - \help", reply_markup=key)
	elif message.text == "пока":
		bot.send_message(message.chat.id, "Ответ на 'пока'")
	else:
		bot.send_message(message.chat.id, message.text+"\nID: "+str(message.from_user.id))


time.sleep(0.5)
bot.polling()
