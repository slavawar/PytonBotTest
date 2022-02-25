import os

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):
    response = data.get_request(_user["resive_token"], 'https://hrw.test.urentbike.ru:10005', 'activity')
    if response == 401: return
    
    _transport = []
    for transport in response['activities']:
        _transport.append(transport['bikeIdentifier'])
    if _transport == []: text = 'Нет транспорта в аренде.'
    else: text = "Список транспорта в аренде:\n" + "\n".join(_transport)
    bot.send_message(message.from_user.id, text)