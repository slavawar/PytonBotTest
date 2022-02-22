import os

import dotenv
from func import data;
from dotenv import load_dotenv, find_dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def funca(message, collection, bot, _user):
    Identifier = "S.2009"
    _data = {"locationLat": 55.7073658,
        "locationLng": 37.46039,
        "isQrCode": True,
        "rateId": "60fea631b60b85f19c993c9e",
        "Identifier": Identifier,
        "withInsurance": False
        }
    response = data.post_request('https://hrw.test.urentbike.ru/gatewayclient/api/v1/order/make', _data, os.environ["TOKEN_CRM"])
    print(response)
    if response == False:
        bot.send_message(message.from_user.id, "Что то пошло не так.")
        return
    if response == 401:
        bot.send_message(message.from_user.id, "Токен устарел\nперезапросите командой: /token")
        return
    if (response['succeeded'] == False):
        bot.send_message(message.from_user.id, response['errors'][0]['value'][0])
    else:
        bot.send_message(message.from_user.id, f"Транспорт {Identifier} взят в аренду.")
    