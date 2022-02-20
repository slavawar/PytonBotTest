from telebot import types

# TODO: Возможно привязать тэги.
tag = ['help', 'помощь']
button = []

def funca(message, collection, bot, _user):
    bot.send_message(message.from_user.id, 
            "Вот список моих команд:" + 
            "\n/help - вывести список команд" + 
            "\n/list - Список пользователей" + 
            "\n/profile - Профиль" +
            "\n/reg - Регистрация" +
            "\n/test - Тест")