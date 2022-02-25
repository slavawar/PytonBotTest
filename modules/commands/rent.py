import re
from func import data;

def funca(message, collection, bot, _user):
    try:
        _Identifier = message.text.split(" ")[1]
        match = re.search(r'^S\.([0-9]+)', _Identifier)

        response = data.get_request(_user['resive_token'], 'https://hrw.test.urentbike.ru:10001', 'bikes/identifier/' + _Identifier)
        if (response['succeeded'] == True):

            locked = response['state']['state']['locked']
            connected = response['state']['state']['connected']
            disabled = response['state']['state']['disabled']
            isServiceMode = response['isServiceMode']
            ordered = response['order']['ordered']
            disabledReason = response['state']['disabledReason']
            
            if connected == False:
                bot.send_message(message.from_user.id, "Транспорт не на связи")
                return
            if ordered == True:
                bot.send_message(message.from_user.id, "Транспорт уже Арендован.")
                return
            if disabledReason:
                bot.send_message(message.from_user.id, "Транспорт снят с доступа.")
                return
            if isServiceMode == True:
                bot.send_message(message.from_user.id, "Транспорт в сервисном режиме.")
                return
            if locked == False:
                bot.send_message(message.from_user.id, "Транспорт открыт, закройте его.")
                return
            
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
            
        else:
            bot.send_message(message.from_user.id, "Введите команду в формате: /rent S.XXXX")

    except Exception:
        bot.send_message(message.from_user.id, f"Введите команду в формате: /rent S.XXXX")
        return