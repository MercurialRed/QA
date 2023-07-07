import telebot
from telebot import types
import requests


class new_joke():

    def __init__(self):
        pass

TOKEN = "TOKEN"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👉 Gimme a Fact! 👈")

    markup.add(item1)

    bot.send_message(message.chat.id,
                     "Here for a new fact about me, {0.first_name}?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def fact(message):
    url = "https://api.chucknorris.io/jokes/random"
    result = requests.get(url)
    result.encoding = "utf-8"
    check = result.json()
    check_value = check.get("value")
    print(check_value)
    if message.chat.type == 'private':
        if message.text == '👉 Gimme a Fact! 👈':
            bot.send_message(message.chat.id, check_value)

bot.polling(none_stop=True)
