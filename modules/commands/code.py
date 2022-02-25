import os
import re
from func import data;
import requests

def funca(message, collection, bot, _user):
    try:
        _code = message.text.split(" ")[1]
        match = re.search(r'^([\d]+)$', _code)
        if match == None:
            bot.send_message(message.from_user.id, "Код должен состоять только из цифр!\nПример: /code 1234")
            return
        response = requests.post(
            url = 'https://hrw.test.urentbike.ru/identity/connect/token',
            data = {'client_id':'mobile.client',
                'client_secret': os.getenv('CLIENT_SECRET'),
                'username'     : str(_user['phone']), # TODO: Перевести phone в string. Нет необходимости в integer.
                'password'     : _code,
                'scope'        : 'bike.api ordering.api location.api customers.api payment.api maintenance.api notification.api log.api ordering.scooter.api driver.bike.lock.offo.api driver.scooter.ninebot.api offline_access', 
                'grant_type'   : 'password'},
            headers = {'Environment-Info'   : 'plt:ios,0.46.4,mod:iPhone 6,os:12.1.2,phone:79991001010',
                'User-Agent'                : 'PostmanRuntime/7.29.0',
                'Accept'                    : '*/*',
                'TraceId'                   : '6OHPFK1ENY',
                'X-AppsFlyer-Id'            : '1577185931367-5301174492424016623',
                'X-AppsFlyer-Advertising-Id': '5eaed67d-2c8d-41f3-9167-b6504ca5a95c',
                'Content-Type'              : 'application/x-www-form-urlencoded',
                'Connection'                : 'Keep-Alive',
                'Accept-Encoding'           : 'gzip',
                'User-Agent'                : 'okhttp/3.12.6'}
        )
        if response.status_code == 200:
            resive_token = response.json()['access_token']
            refresh_token = response.json()['refresh_token']
            data.update_document(collection, {'uid': message.from_user.id}, {'resive_token': resive_token, 'refresh_token': refresh_token})
            bot.send_message(message.from_user.id, f"Код подтвержден, токен получен.\nИспользуйте команду /help\nДля получения полного списка команд.")
            return
        if (response.json()['error'] == 'invalid_grant'):
            bot.send_message(message.from_user.id, 'Ошибка: ' + response.json()['error_description'])
            return
        else:
            bot.send_message(message.from_user.id, f"Введите команду в формате: \"/code\" или \"/code 1234\"")
            return False
    
    except Exception:
        response = requests.post(
            url = 'https://hrw.test.urentbike.ru/identity/api/mobile/code',
            headers = {'Environment-Info'   : 'platform: Android, osVersion: 23, appVersion: 1.0.0, device: HRW AutoBot',
                'TraceId'                   : '6OHPFK1ENY',
                'X-AppsFlyer-Id'            : '1577185931367-5301174492424016623',
                'X-AppsFlyer-Advertising-Id': '5eaed67d-2c8d-41f3-9167-b6504ca5a95c',
                'Accept-Language'           : 'ru-RU',
                'Content-Type'              : 'application/json',
                'Connection'                : 'Keep-Alive',
                'Accept-Encoding'           : 'gzip',
                'User-Agent'                : 'okhttp/3.12.6'},
            json = {
                "osVersion"  : "1.0.0",
                "phoneModel" : "HRW AutoBot",
                "phoneNumber": str(_user['phone']),
                "uniqueId"   : "26cc6e0812da1f9e"
            }
        )
        if response.status_code == 200:
            bot.send_message(message.from_user.id, "Запрос смс отправлен!\nПодтвердите код командой: /code 1234")
            return
        if (response.json()['succeeded'] == False or response.status_code == 400):
            bot.send_message(message.from_user.id, 'Ошибка: ' + response.json()['errors'][0]['value'][0])
            return
        else: 
            bot.send_message(message.from_user.id, "Что-то пошло нет." + response.json()['errors'][0]['value'][0])
            return