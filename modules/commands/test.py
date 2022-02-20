from telebot import types

tag = ['test', 'тест']
button = []

def funca(message, collection, bot, _user):
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    base_url = "https://hrw.test.urentbike.ru"
    key_hrw = types.InlineKeyboardButton(text='hrw.test', callback_data='hrw', url=base_url);
    keyboard.add(key_yes).add(key_no).add(key_hrw);
    question = 'Вот клавиатура:';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)