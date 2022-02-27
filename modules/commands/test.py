import os, pathlib

def funca(message, collection, bot, _user):
    os.chdir(os.getcwd() + "/tests")
    os.system('python runner.py')

    bot.send_message(message.from_user.id, "Тесты запущены.")