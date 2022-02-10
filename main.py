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

@bot.message_handler(content_types=['text'])
def get_text_messages(message): 
    messages.get_text_messages(message, collection, bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call): 
    keyboard.callback_worker(call, bot)

bot.polling(none_stop=True, interval=0)