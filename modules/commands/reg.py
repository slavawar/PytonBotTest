import re
from telebot import types
from func import data;

def funca(message, collection, bot, _user):
    if (_user != None):
        bot.send_message(message.from_user.id, "Ты уже зарегистрирован!")
        return

    if (_user == None and message.text == "/reg"):
        bot.send_message(message.from_user.id, 'Привет!\nВведи свой номер телефона в формате:\n/reg 79654690221')
        return

    if _user == None:
        try:
            _phone = message.text.split(" ")[1]
            match = re.search(r'^([\d]{11})$', _phone)
            if match == None:
                bot.send_message(message.from_user.id, 'Номер телефона должен состоять из 11 цифр!')
                return
            # Проверяем что такой номер уже существует.
            _test_phone = data.find_document(collection, {'phone': int(_phone)})
            if _test_phone != None:
                bot.send_message(message.from_user.id, 'Такой номер уже существует, попробуй другой!')
                return

            count_users = collection.count_documents({})
            reg = { "id": count_users + 1,
                "uid"   : message.from_user.id,
                "name"  : message.from_user.first_name,
                "phone" : int(_phone),
                "resive_token"  : "",
                "refresh_token" : ""}
            data.insert_document(collection, reg)
            bot.send_message(message.from_user.id, message.from_user.first_name + ', твой номер "' + _phone + '" сохранен!\nТы успешно зарегистрирован!\n/help - получить список всех команд.')
            return

        except Exception:
            bot.send_message(message.from_user.id, 'Привет!\nВведи свой номер телефона в формате:\n/reg 79654690221')
            return