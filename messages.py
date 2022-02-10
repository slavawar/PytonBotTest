import func;
from telebot import types

def get_text_messages(message, collection, bot):
    # Логирование сообщений
    print(f'Принято новое сообщение: "{message.text}", От {message.from_user.first_name} {message.from_user.last_name}')

    # Запрашиваем профиль пользователя
    _user = func.find_document(collection, {'uid': message.from_user.id})

    if (_user == None and message.text != "/reg"):
        bot.send_message(message.from_user.id, 'Ты не зарегистрирован!\nИспользуй команду: /reg')
        return

    match message.text:
        case "/reg":
            if (_user != None):
                bot.send_message(message.from_user.id, "Ты уже зарегистрирован!")
                return
            count_users = collection.count_documents({})
            reg = { "id": count_users + 1, "uid": message.from_user.id, "name": message.from_user.first_name }
            func.insert_document(collection, reg)
            bot.send_message(message.from_user.id, "Ты успешно зарегистрирован!")
            return

        case "/тест":
            keyboard = types.InlineKeyboardMarkup();
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
            base_url = "https://hrw.test.urentbike.ru"
            key_no = types.InlineKeyboardButton(text='Нет', callback_data='no', url=base_url);
            keyboard.add(key_yes).add(key_no);
            question = 'Вот клавиатура:';
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        
        case "/start":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\nВведи: /help, что-бы получить список команд!")

        case "/help":
            bot.send_message(message.from_user.id, 
            "Вот список моих команд:" + 
            "\n/help - вывести список команд" + 
            "\n/list - Список пользователей" + 
            "\n/profile - Профиль" +
            "\n/reg - Регистрация")

        case "/profile":
            bot.send_message(message.from_user.id, 
            '\nТвой профиль,' + 
            f'\nИмя: {_user["name"]}' +
            f'\nID Профиля: {str(_user["id"])}')

        case "/list":
            users = func.find_document(collection, {}, True)
            list = ''
            for user in users:
                list = f'{list}[{user["id"]}] {user["name"]}\n'
            bot.send_message(message.from_user.id, f'Список пользователей в базе:\n{list}')

        case _:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help, что-бы получить список моих команд.")