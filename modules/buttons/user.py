from telebot import types

def function(call, collection, bot, _user):
    match call.data.split("_")[1]:
        case "ACCEPT":
            bot.send_message(call.from_user.id, 'Ты ответил да?');

        case "DECLINE":
            bot.send_message(call.from_user.id, 'Ты ответил нет?');