import os
import re
from func import data;
from importlib.machinery import SourceFileLoader

def get_text_messages(message, collection, bot):
    # Логирование сообщений. (в консоль, для личных целей, не несет смысла)
    print(f'Принято новое сообщение: "{message.text}", От {message.from_user.first_name} {message.from_user.last_name}')

    # Запрашиваем профиль пользователя в базе.
    _user = data.find_document(collection, {'uid': message.from_user.id})

    # Проверка на существующую запись пользователя в базе.
    if (_user == None and not re.search(r'(\/reg)', message.text)):
        bot.send_message(message.from_user.id, 'Ты не зарегистрирован!\nИспользуй команду: /reg')
        return
    if _user != None:
        test = data.ini_token(message, collection, bot, _user)
        if test == True: _user = data.find_document(collection, {'uid': message.from_user.id})

    match = re.search(r'^\/(.*)', message.text)
    if match:
        # Обработчик команд.
        try:
            link = re.search(r'(.*)\s(.*)', match[1])
            if link: _command = link[1]
            else: _command = match[1]
            folder = os.getcwd() + '\modules\commands\\' + _command + '.py'
            foo = SourceFileLoader(match[1],folder).load_module()
            foo.funca(message, collection, bot, _user)
        
        except Exception:
            bot.send_message(message.from_user.id, "Неизвестная команда. Напиши /help, что-бы получить список моих команд.")
        
    else:
        # TODO: Тут должен быть обработчик на фразы или список возможных.
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help, что-бы получить список моих команд.", reply_to_message_id=message.id)