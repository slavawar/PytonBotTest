from importlib.machinery import SourceFileLoader
import func;
import os

def callback_worker(call, bot, collection):

    _user = func.find_document(collection, {'uid': call.from_user.id})

    try:
        test = call.data.split("_")
        folder = os.getcwd() + '\modules\\buttons\\' + test[0] + '.py'
        foo = SourceFileLoader(test[0],folder).load_module()
        foo.function(call, collection, bot, _user)
        
    except Exception:
        bot.send_message(call.message.chat.id, "Неизвестная кнопка.")