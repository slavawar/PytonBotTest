def callback_worker(call, bot):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Ты ответил да?');
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Ты ответил нет?');