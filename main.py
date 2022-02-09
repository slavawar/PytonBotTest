from pymongo import MongoClient;
import telebot;
import setting;
import keyboard;
import messages;

bot = telebot.TeleBot(setting.token);

client = MongoClient(setting.mongoUrl)
db = client['PytonTestBot']
collection = db['bot']

@bot.message_handler(content_types=['text'])
def get_text_messages(message): 
    messages.get_text_messages(message, collection, bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call): 
    keyboard.callback_worker(call, bot)

bot.polling(none_stop=True, interval=0)