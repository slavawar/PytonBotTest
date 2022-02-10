def callback_worker(call, bot):
    match call.data:
        case "yes":
            bot.send_message(call.message.chat.id, 'Ты ответил да?');

        case "no":
            bot.send_message(call.message.chat.id, 'Ты ответил нет?');