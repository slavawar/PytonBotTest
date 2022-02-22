import os
import re

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):
    try:
        _Identifier = message.text.split(" ")[1]
        match = re.search(r'^S\.([0-9]+)', _Identifier)
    
        _data = {"locationLat": 43.4517473333,
            "locationLng": 39.9129041667,
            "Identifier": match[1]
        }
        response = data.post_request('https://hrw.test.urentbike.ru/gatewayclient/api/v1/order/end', _data, os.environ["TOKEN_CRM"])
        print(response)
        if response == False:
            bot.send_message(message.from_user.id, "Что то пошло не так.")
            return
        if response == 401:
            bot.send_message(message.from_user.id, "Токен устарел\nперезапросите командой: /token")
            return
        if (response['succeeded'] == False):
            bot.send_message(message.from_user.id, 'test: ' + response['errors'][0]['value'][0])
        else:
            bot.send_message(message.from_user.id, f"Вы завершили аренду у {match[1]}")
        return

    except Exception:
        bot.send_message(message.from_user.id, f"Введите команду в формате: /endrent S.XXXX")
        return
    