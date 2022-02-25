from telebot import types

def funca(message, collection, bot, _user):
    bot.send_message(message.from_user.id, 
            "Вот список моих команд:" + 
            "\n/profile - Профиль" + 
            "\n/reg - Регистрация" +
            "\n/code - Подтверждение смс кода" +
            "\n/rent [ID] - Взять ТС в аренду" +
            "\n/endrent [ID] - Завершить аренду" +
            "\n/activity - Список арендованных ТС")