from telebot import types

tag = ['profile', 'профиль']
button = []

def funca(message, collection, bot, _user):
    bot.send_message(message.from_user.id, 
            '\nТвой профиль,' + 
            f'\nИмя: {_user["name"]}' +
            f'\nID Профиля: {str(_user["id"])}')