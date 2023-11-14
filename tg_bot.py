import telebot
import parse


f = open('token')
token = f.read()

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message , "Wazzaaaap")

@bot.message_handler(func=lambda m :True)

def echo_all(message):
    dictionary = parse.string_to_json(message.text)
    print(dictionary)


bot.infinity_polling()