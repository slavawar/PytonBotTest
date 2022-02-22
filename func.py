import requests

class data:
    # Добавление записи
    def insert_document(collection, data):
        return collection.insert_one(data).inserted_id

    # Чтение записи
    def find_document(collection, elements, multiple=False):
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            return collection.find_one(elements)

    # Обновление записи
    # update_document(series_collection, {'_id': id_}, {'name': 'Name'})
    def update_document(collection, query_elements, new_values):
        collection.update_one(query_elements, {'$set': new_values})

    # Удаление записи
    def delete_document(collection, query):
        collection.delete_one(query)

    def post_request(_url, data, access_token):
        response = requests.post(
            url = _url,
            json = data,
            headers = {'Host'     : 'test.urentbike.ru:10012',
                'Accept'          : '*/*',
                'Authorization'   : 'Bearer ' + access_token,
                'Connection'      : 'keep-alive',
                'Environment-Info': 'plt:ios,0.46.4,mod:iPhone 6,os:12.1.2,phone:79991001010',
                'Accept-Language' : 'ru-RU',
                'Accept-Encoding' : 'gzip',
                'X-AppsFlyer-Id'  : '1577364586097-9492869',
                'charset'         : 'UTF-8',
                'TraceId'         : '7KEQXVDE5N',
                'User-Agent'      : 'UrentbikeTest/0.46.4 (ru.urentbike.app.test; build:464; iOS 12.1.2) Alamofire/4.9.1',
                'X-AppsFlyer-Idfa': 'ABDBBF0F-41C8-42ED-9C9E-5716BB73E837',
                'Content-Type'    : 'application/json'}
        )
        if (response.status_code == 200 or response.status_code == 400):
            return response.json()
        if response.status_code == 401:
            return 401
        else: return False

    def get_request(access_token, url, service):
        response = requests.get(
            url + '/api/' + service,
            headers = {'Host'     : 'test.urentbike.ru:10005',
                'Accept'          : '*/*',
                'Authorization'   : 'Bearer ' + access_token,
                'Connection'      : 'keep-alive',
                'Environment-Info': 'plt:ios,0.46.4,mod:iPhone 6,os:12.1.2,phone:79991001010',
                'Accept-Language' : 'ru-RU',
                'Accept-Encoding' : 'gzip;q=1.0, compress;q=0.5',
                'X-AppsFlyer-Id'  : '1577364586097-9492869',
                'charset'         : 'UTF-8',
                'User-Agent'      : 'UrentbikeTest/0.46.4 (ru.urentbike.app.test; build:464; iOS 12.1.2) Alamofire/4.9.1',
                'Content-Type'    : 'application/json',
                'X-AppsFlyer-Idfa': 'ABDBBF0F-41C8-42ED-9C9E-5716BB73E837'},
        )
        if (response.status_code == 200 or response.status_code == 400): return response.json()
        if response.status_code == 401:
            return 401
        else: return False

    def code_request():
        response = requests.post(
            url = 'https://hrw.test.urentbike.ru/identity/api/mobile/code',
            headers = {'Environment-Info'   : 'platform: Android, osVersion: 23, appVersion: 0.43.2 (217), device: Xiaomi Redmi 4',
                'TraceId'                   : '6OHPFK1ENY',
                'X-AppsFlyer-Id'            : '1577185931367-5301174492424016623',
                'X-AppsFlyer-Advertising-Id': '5eaed67d-2c8d-41f3-9167-b6504ca5a95c',
                'Authorization'             : 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImUzYzkxOTUwMmRjNTg3NzM5YjJiNzM2MTEwY2M5M2Q0IiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NzcxODU5ODcsImV4cCI6MTU3NzE4Nzc4NywiaXNzIjoiaHR0cHM6Ly9zZXJ2aWNlLnVyZW50YmlrZS5ydToxMDAwMCIsImF1ZCI6WyJodHRwczovL3NlcnZpY2UudXJlbnRiaWtlLnJ1OjEwMDAwL3Jlc291cmNlcyIsImJpa2UuYXBpIiwiY3VzdG9tZXJzLmFwaSIsImRyaXZlci5iaWtlLmxvY2sub2Zmby5hcGkiLCJkcml2ZXIuc2Nvb3Rlci5uaW5lYm90LmFwaSIsImxvY2F0aW9uLmFwaSIsImxvZy5hcGkiLCJtYWludGVuYW5jZS5hcGkiLCJub3RpZmljYXRpb24uYXBpIiwib3JkZXJpbmcuYXBpIiwib3JkZXJpbmcuc2Nvb3Rlci5hcGkiLCJwYXltZW50LmFwaSJdLCJjbGllbnRfaWQiOiJtb2JpbGUuY2xpZW50Iiwic2NvcGUiOlsiYmlrZS5hcGkiLCJjdXN0b21lcnMuYXBpIiwiZHJpdmVyLmJpa2UubG9jay5vZmZvLmFwaSIsImRyaXZlci5zY29vdGVyLm5pbmVib3QuYXBpIiwibG9jYXRpb24uYXBpIiwibG9nLmFwaSIsIm1haW50ZW5hbmNlLmFwaSIsIm5vdGlmaWNhdGlvbi5hcGkiLCJvcmRlcmluZy5hcGkiLCJvcmRlcmluZy5zY29vdGVyLmFwaSIsInBheW1lbnQuYXBpIl19.lBbzOa5wyCDTCpbqMjx5ugebNWIJpU92IkrDGnQ1mtgxTwHndw_qmJu-JnA_THtFM7cnq1_Q3UY-VCs3-NXjQOz6NwwmNQcdq2DO2e0v-DOAl3Eedo5fEZYcfVVLfCvzZAEerl4y8RxlWxejxXR37wo5S6GCZq0tQ9e8MCsvbhqiM9Kysdo7t_qcQJecj4R_BGtn78ftHvBWJpAin0GM-i-tacGFlOmf7QHn2W30XDVNFx2wpgk9pOAyAklKrbrHs8JD3ytAbPhZrGbq1yVPLYJwt0uj_aCl_IqrWH2GEZ04FShGuof5pZNRp9DlYJb_rc0OzE2AFBn5KpmjNQm0HA',
                'Accept-Language'           : 'ru-RU',
                'Content-Type'              : 'application/json',
                'Connection'                : 'Keep-Alive',
                'Accept-Encoding'           : 'gzip',
                'User-Agent'                : 'okhttp/3.12.6'},
            json = {
                "osVersion":"6.0.1",
                "phoneModel":"Xiaomi Xiaomi markw",
                "phoneNumber":"79654690221",
                "uniqueId":"26cc6e0812da1f9e"
            }
        )
        if (response.status_code == 200 or response.status_code == 400):
            return response.json()
        else: return False

    def token_request():
        response = requests.post(
            url = 'https://hrw.test.urentbike.ru/identity/connect/token',
            data = {'client_id':'mobile.client',
                'client_secret': 'caRgg4LIWUsjOz9u1r8oLIpiJU8VcifabXVWLJy5bMPjqtE6ZMfTHn7ykpmJR8uz',
                'username'     : '79654690221',
                'password'     : '1010',
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
        if (response.status_code == 200 or response.status_code == 400): return response.json()
        else: return False