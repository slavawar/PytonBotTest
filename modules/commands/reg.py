from telebot import types
from func import data;

# TODO: Возможно привязать тэги.
tag = ['reg', 'регистрация']
button = []

def funca(message, collection, bot, _user):
    if (_user != None):
        bot.send_message(message.from_user.id, "Ты уже зарегистрирован!")
        return
    count_users = collection.count_documents({})
    reg = { "id": count_users + 1, "uid": message.from_user.id, "name": message.from_user.first_name }
    data.insert_document(collection, reg)
    bot.send_message(message.from_user.id, "Ты успешно зарегистрирован!")
    return