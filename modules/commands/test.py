from telebot import types

tag = ['test', 'тест']
button = []

def funca(message, collection, bot, _user):
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='USER_ACCEPT');
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='USER_DECLINE');
    keyboard.add(key_yes).add(key_no);
    question = 'Вот кнопки';
    bot.send_message(message.from_user.id, text = question, reply_markup = keyboard)