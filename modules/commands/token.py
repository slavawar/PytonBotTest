import os

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):
    test = data.code_request()
    if test == False: bot.send_message(message.from_user.id, "Упал запрос.")

    if test['succeeded'] == True:
        token = data.token_request()
        os.environ['TOKEN_CRM'] = token['access_token']
        dotenv.set_key(dotenv_file, "TOKEN_CRM", os.environ["TOKEN_CRM"])

        bot.send_message(message.from_user.id, "Новый токен получен.")
    else:
        print(test['errors'][0])
        bot.send_message(message.from_user.id, "Таймаут, перезапросите чуть позже.")