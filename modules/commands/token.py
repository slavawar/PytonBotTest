import os

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):

    #TODO: Навернуть обновление токена.
    bot.send_message(message.from_user.id, "Новый токен получен.")