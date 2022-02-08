from pymongo import MongoClient;
import telebot;
import setting;
import func;

bot = telebot.TeleBot(setting.token);

client = MongoClient(setting.mongoUrl)
db = client['PytonTestBot']
series_collection = db['bot']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Логирование сообщений
    print('Принято новое сообщение:', '"' + message.text + '",', "От:", str(message.from_user.id))

    # Запрашиваем профиль пользователя
    result = func.find_document(series_collection, {'uid': message.from_user.id})

    if (result == None and message.text != "/reg"):
        bot.send_message(message.from_user.id, 'Ты не зарегистрирован!\nИспользуй команду: /reg')
        return

    if (message.text == "/reg"):
        if (result != None):
            bot.send_message(message.from_user.id, "Ты уже зарегистрирован!")
            return
        mydoc = series_collection.count_documents({})
        reg = { "id": mydoc + 1, "uid": message.from_user.id, "name": message.from_user.first_name }
        func.insert_document(series_collection, reg)
        bot.send_message(message.from_user.id, "Ты успешно зарегистрирован!")
        return

    if (message.text == "/start"):
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?\nВведи: /help, что-бы получить список команд!")

    if (message.text == "/help"):
        bot.send_message(message.from_user.id, "Вот список моих команд:" + 
        "\n/help - вывести список команд" + 
        "\n/list - Список пользователей" + 
        "\n/profile - Профиль" +
        "\n/reg - Регистрация")

    if (message.text == "/profile"):        
        bot.send_message(message.from_user.id, 
            "\nТвой профиль," + 
            "\nИмя: " + result['name'] +
            "\nID Профиля: " + str(result['id'])
        )

    if message.text == "/list":
        users = func.find_document(series_collection, {}, True)
        list = ''
        for user in users:
            list = list + '[' + str(user['id']) + '] ' + user['name'] + '\n'
        bot.send_message(message.from_user.id, "Список пользователей в базе:\n" + list)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help, что-бы получить список моих команд.")

bot.polling(none_stop=True, interval=0)