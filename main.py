from pymongo import MongoClient;
import telebot;
import setting;
import func;

bot = telebot.TeleBot(setting.token);

client = MongoClient(setting.mongoUrl)
db = client['PytonTestBot']
collection = db['bot']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Логирование сообщений
    print('Принято новое сообщение:', '"' + message.text + '",', "От:", message.from_user.first_name, message.from_user.last_name)

    # Запрашиваем профиль пользователя
    _user = func.find_document(collection, {'uid': message.from_user.id})

    if (_user == None and message.text != "/reg"):
        bot.send_message(message.from_user.id, 'Ты не зарегистрирован!\nИспользуй команду: /reg')
        return

    if (message.text == "/reg"):
        if (_user != None):
            bot.send_message(message.from_user.id, "Ты уже зарегистрирован!")
            return
        count_users = collection.count_documents({})
        reg = { "id": count_users + 1, "uid": message.from_user.id, "name": message.from_user.first_name }
        func.insert_document(collection, reg)
        bot.send_message(message.from_user.id, "Ты успешно зарегистрирован!")
        return

    elif (message.text == "/start"):
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\nВведи: /help, что-бы получить список команд!")

    elif (message.text == "/help"):
        bot.send_message(message.from_user.id, "Вот список моих команд:" + 
        "\n/help - вывести список команд" + 
        "\n/list - Список пользователей" + 
        "\n/profile - Профиль" +
        "\n/reg - Регистрация")

    elif (message.text == "/profile"):        
        bot.send_message(message.from_user.id, 
            "\nТвой профиль," + 
            "\nИмя: " + _user['name'] +
            "\nID Профиля: " + str(_user['id'])
        )

    elif message.text == "/list":
        users = func.find_document(collection, {}, True)
        list = ''
        for user in users:
            list = list + '[' + str(user['id']) + '] ' + user['name'] + '\n'
        bot.send_message(message.from_user.id, "Список пользователей в базе:\n" + list)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help, что-бы получить список моих команд.")

bot.polling(none_stop=True, interval=0)