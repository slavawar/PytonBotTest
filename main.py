from pymongo import MongoClient;
import telebot;
import keyboard;
import messages;
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN')); 
client = MongoClient(os.getenv('MONGO_URL'))
db = client['PytonTestBot']
collection = db['bot']

# Обработка полученного текстового сообщения, вызов модуля messages.py
@bot.message_handler(content_types=['text'])
def get_text_messages(message): 
    messages.get_text_messages(message, collection, bot)

# Обработка нажатой кнопки, вызов модуля keyboard.py
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call): 
    keyboard.callback_worker(call, bot, collection)

bot.polling(non_stop=True, interval=0)