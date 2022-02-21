from telebot import types
import func;

button = []

def function(call, collection, bot, _user):
    test = call.data.split("_")
    match test[1]:
        case "ACCEPT":
            bot.send_message(call.from_user.id, 'Ты ответил да?');

        case "DECLINE":
            bot.send_message(call.from_user.id, 'Ты ответил нет?');