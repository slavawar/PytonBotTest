import os

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):
    response = data.get_request(os.environ["TOKEN_CRM"], 'https://hrw.test.urentbike.ru:10005', 'activity')
    print(response)
    if response == 401:
        bot.send_message(message.from_user.id, "Токен устарел\nперезапросите командой: /token")
        return
    
    bot.send_message(message.from_user.id, "Что то есть.")