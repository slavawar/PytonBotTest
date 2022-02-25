import re
from func import data;

def funca(message, collection, bot, _user):
    try:
        _Identifier = message.text.split(" ")[1]
        match = re.search(r'^S\.([0-9]+)', _Identifier)
        
        _data = {"locationLat": 43.4517473333,
            "locationLng": 39.9129041667,
            "isQrCode": True,
            "rateId": "5f292e7e124abe0001ced7eb",
            "Identifier": match[1],
            "withInsurance": False
            }
        response = data.post_request('https://hrw.test.urentbike.ru/gatewayclient/api/v1/order/make', _data, _user["resive_token"])
        if response == False:
            bot.send_message(message.from_user.id, "Что то пошло не так.")
            return
        if response == 401:
            bot.send_message(message.from_user.id, "Токен устарел\nперезапросите командой: /token")
            return
        if (response['succeeded'] == False):
            bot.send_message(message.from_user.id, 'test: ' + response['errors'][0]['value'][0])
        else:
            bot.send_message(message.from_user.id, f"Транспорт {match[1]} взят в аренду.")
    
    except Exception:
        bot.send_message(message.from_user.id, f"Введите команду в формате: /rent S.XXXX")
        return