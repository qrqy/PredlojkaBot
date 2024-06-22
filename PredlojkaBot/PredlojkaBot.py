import telebot
from telebot import types

bot = telebot.TeleBot('7470913385:AAG2-XxkGnQldq9MSdGMtAkb6fk26xXLRnM')
adminID = 1248220310

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет, я предложка-бот канала [qrqy freak](https://t.me/qrqysus). Если ты хочешь предложить новость, отправь мне текст, фото или видео. Я отправлю его на модерацию и в ближайшее время ты увидишь пост в тгк!", parse_mode='Markdown')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('О канале')
    btn2 = types.KeyboardButton('Сделать пост')
    btn3 = types.KeyboardButton('Немного про автора')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, 'Тыкни на кнопку если нада', reply_markup=markup) #ответ бота
    if message.from_user.id!=adminID:
        bot.send_message(adminID, "New chat with"+message.from_user.id, parse_mode='Markdown');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

        


    if message.text == 'Немного про автора':
        bot.send_message(message.from_user.id, 'Канал [qrqy freak](https://t.me/qrqysus) - это моя телега [qrqy](https://t.me/qrqys). Я мамкин программист с айти специальностью (закончил СПО, планирую вышку), уже больше года работаю по профессии, чем очень даже горжусь, играю в разные игрульки, такие как Minecraft, HS:BG и CS 2', parse_mode='Markdown')
    elif message.text == 'О канале':
        bot.send_message(message.from_user.id, 'Канал [qrqy freak](https://t.me/qrqysus) - это моя телега, тут я пощу мемчики в основном, немного контента из жизни, а так же уведомления о стримах (ой, когда-нибудь буду стримить)', parse_mode='Markdown')
    elif message.text == 'Сделать пост':
        bot.send_message(message.from_user.id, 'Сделай пост, чтобы вызвать кнопки помощи юзани команду старт', parse_mode='Markdown')
@bot.message_handler(content_types=['video'])
def get_video_messages(message):
    bot.send_message(1248220310, message.video, parse_mode='Markdown');
    bot.send_message(1248220310, message.from_user.id, parse_mode='Markdown');
    

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть