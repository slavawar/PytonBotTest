from telebot import types
import func;

tag = ['list', 'список']
button = []

def funca(message, collection, bot, _user):
    users = func.find_document(collection, {}, True)
    list = ''
    for user in users:
        list = f'{list}[{user["id"]}] {user["name"]}\n'
    bot.send_message(message.from_user.id, f'Список пользователей в базе:\n{list}')