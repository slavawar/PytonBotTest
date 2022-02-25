import time
import jwt

def funca(message, collection, bot, _user):
    decode_jwt_info = jwt.decode(
        _user["resive_token"],
        algorithms="HS256",
        options={"verify_signature": False}
    )
    exp = decode_jwt_info['exp']
    _time = int(time.time())

    if _time > exp:
        bot.send_message(message.from_user.id, "Пора обновить токен.")
    else:
        bot.send_message(message.from_user.id, "С токеном все ок, пользуемся дальше.")