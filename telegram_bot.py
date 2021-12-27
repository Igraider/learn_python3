import telebot
from random import choice
Token = ''
bot = telebot.TeleBot(Token)

hello_stickers = ['learn_python3/hel_sticker.tgs', 'learn_python3/snowman_sticker.tgs', 'learn_python3/hel_moroz.tgs']

@bot.message_handler(commands=['start', 'help'])
def sendWelcome(message):
    hello_sticker = open(choice(hello_stickers), 'rb')
    bot.send_sticker(message.chat.id, hello_sticker)
    bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name) + '!')
    bot.send_message(message.chat.id, 'Меня зовут ' + str(bot.get_me().first_name) + ', вот мои функции:')


bot.polling()