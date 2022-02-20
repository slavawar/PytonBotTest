from telebot import types

tag = ['start']
button = []

def funca(message, collection, bot, _user):
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\nВведи: /help, что-бы получить список команд!")