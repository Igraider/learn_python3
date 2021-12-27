import telebot
from random import choice
Token = ''
bot = telebot.TeleBot(Token)

hello_stickers = ['learn_python3/hel_sticker.tgs', 'learn_python3/snowman_sticker.tgs', 'learn_python3/hel_moroz.tgs'] #Стикеры
bye_stickers = ['learn_python3/hel_sticker.tgs', 'learn_python3/dedbye.tgs', 'learn_python3/snowmanbyesticker.tgs']    #Стикеры
sightspin = 'learn_python3/sight_spin.jpg'
downspin = 'learn_python3/down_spin.jpg'
topspin = 'learn_python3/top_spin.jpg'

@bot.message_handler(commands=['start', 'help']) #Команды
def sendWelcome(message):
    hello_sticker = open(choice(hello_stickers), 'rb') #Выбор случайного стикера с приветствием
    bot.send_sticker(message.chat.id, hello_sticker)
    bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name) + '!')
    bot.send_message(message.chat.id, 'Меня зовут ' + str(bot.get_me().first_name) + ', вот мои функции:')
    bot.send_message(message.chat.id, '/pitch - виды подач.')
    bot.send_message(message.chat.id, '/end или /finish - завершить работу.')

@bot.message_handler(commands=['pitch'])
def sendPitches(message):
    sight = open(sightspin, 'rb')
    bot.send_photo(message.chat.id, sight)
    bot.send_message(message.chat.id, '1. Боковое вращение.')
    down = open(downspin, 'rb')
    bot.send_photo(message.chat.id, down)
    bot.send_message(message.chat.id, '2. Нижнее вращение.')
    top = open(topspin, 'rb')
    bot.send_photo(message.chat.id, top)
    bot.send_message(message.chat.id, '3. Верхнее вращение.')
    
@bot.message_handler(commands=['end', 'finish']) 
def sayGoodbye(message):
    bye_sticker = open(choice(bye_stickers), 'rb') #Выбор случайного стикера о завершении работы
    bot.send_sticker(message.chat.id, bye_sticker)
    bot.send_message(message.chat.id, 'Пока, удачи ' + str(message.from_user.first_name) + '!')
    
bot.polling()