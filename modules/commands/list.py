from telebot import types
from func import data;

tag = ['list', 'список']
button = []

def funca(message, collection, bot, _user):
    users = data.find_document(collection, {}, True)
    list = ''
    for user in users:
        list = f'{list}[{user["id"]}] {user["name"]}\n'
    bot.send_message(message.from_user.id, f'Список пользователей в базе:\n{list}')