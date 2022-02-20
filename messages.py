import os
import re
import importlib.util as ilu
import func;
from telebot import types
from importlib.machinery import SourceFileLoader

def get_text_messages(message, collection, bot):
    # Логирование сообщений. (в консоль, для личных целей, не несет смысла)
    print(f'Принято новое сообщение: "{message.text}", От {message.from_user.first_name} {message.from_user.last_name}')

    # Запрашиваем профиль пользователя в базе.
    _user = func.find_document(collection, {'uid': message.from_user.id})

    # Проверка на существующую запись пользователя в базе.
    if (_user == None and message.text != "/reg"):
        bot.send_message(message.from_user.id, 'Ты не зарегистрирован!\nИспользуй команду: /reg')
        return

    match = re.search(r'^\/(.*)', message.text)
    if match:
        # Обработчик команд.
        try:
            folder = os.getcwd() + '\modules\commands\\' + match[1] + '.py'
            foo = SourceFileLoader(match[1],folder).load_module()
            foo.funca(message, collection, bot, _user)
        
        except Exception:
            bot.send_message(message.from_user.id, "Неизвестная команда. Напиши /help, что-бы получить список моих команд.")
        
    else:
        # TODO: Тут должен быть обработчик на фразы
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help, что-бы получить список моих команд.")