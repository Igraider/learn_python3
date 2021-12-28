import telebot
from random import choice
Token = ''
bot = telebot.TeleBot(Token)

hello_stickers = ['learn_python3/hel_sticker.tgs', 'learn_python3/snowman_sticker.tgs', 'learn_python3/hel_moroz.tgs'] #Стикеры
bye_stickers = ['learn_python3/hel_sticker.tgs', 'learn_python3/dedbye.tgs', 'learn_python3/snowmanbyesticker.tgs']    #Стикеры
sightspin = 'learn_python3/sight_spin.jpg'
downspin = 'learn_python3/down_spin.jpg'
topspin = 'learn_python3/top_spin.jpg'
verification_pitch = False

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
    global verification_pitch
    verification_pitch = True
    sight = open(sightspin, 'rb')
    bot.send_photo(message.chat.id, sight)
    bot.send_message(message.chat.id, '1. Боковое вращение.')
    down = open(downspin, 'rb')
    bot.send_photo(message.chat.id, down)
    bot.send_message(message.chat.id, '2. Нижнее вращение.')
    top = open(topspin, 'rb')
    bot.send_photo(message.chat.id, top)
    bot.send_message(message.chat.id, '3. Верхнее вращение.')
    bot.send_message(message.chat.id, '''Какую подачу разберем?
Наберите "1", "2" или "3".
    ''')

@bot.message_handler(commands=['end', 'finish']) 
def sayGoodbye(message):
    bye_sticker = open(choice(bye_stickers), 'rb') #Выбор случайного стикера о завершении работы
    bot.send_sticker(message.chat.id, bye_sticker)
    bot.send_message(message.chat.id, 'Пока, удачи ' + str(message.from_user.first_name) + '!')
    
@bot.message_handler(content_types=['text'])
def answerOnMessage(message):

    if message.text == '1' and verification_pitch == True:
        
        bot.send_message(message.chat.id, '1. Топорик.')
        bot.send_message(message.chat.id, '''Перемещая ракетку вправо или влево, игрок придает мячу боковое вращение с вертикальной осью.
Стоит заметить, что не существует чистых видов вращения.
Каждый удар приводит к тому, что мяч начинает двигаться по траектории с верхне-боковым или нижне-боковым вращением.
При ударе ракеткой по мячу, мяч полетит влево или вправо, направление зависит от вращения.''')
        toporik = open('pictures/toporik.jpg', 'rb')
        bot.send_photo(message.chat.id, toporik)
        bot.send_message(message.chat.id, '''Выполняется движением сверху вниз, будто "срубаешь".
Во время удара спортсмен приседает. Топорик имеет как правило боковое-верхнее вращение.''')

        bot.send_message(message.chat.id, '2. Маятник.')
        mayatnic = open('pictures/mayatnik.png', 'rb')
        bot.send_photo(message.chat.id, mayatnic)
        bot.send_message(message.chat.id, 'Выполняя эту подачу, ракетка движется справа на лево и мячу придается левое боковое вращение.')

        bot.send_message(message.chat.id, '3. Подача с обратным боковым вращением.')
        bot.send_message(message.chat.id, 'То же самое что "топорик" и "маятник" только в обратную сторону.')
        reversepic = open('pictures/reversepitch.jpg', 'rb')
        bot.send_photo(message.chat.id, reversepic)

    elif message.text == '2' and verification_pitch == True:

        bot.send_message(message.chat.id, '1. Обычная подрезка.')
        podrezkasleva = open('pictures/podrezkasleva.jpg', 'rb')
        podrezkaspravo = open('pictures/podrezkaspravo.jpg', 'rb')
        bot.send_photo(message.chat.id, podrezkasleva)
        bot.send_photo(message.chat.id, podrezkaspravo)
        bot.send_message(message.chat.id, 'Движение выполняется сверху вниз от плечу к столу, это обычное движение подрезки.')

        bot.send_message(message.chat.id, '2. Веер.')
        fan_pitch = open('pictures/fan_pitch.jpg', 'rb')
        bot.send_photo(message.chat.id, fan_pitch)
        bot.send_message(message.chat.id, '''Рука описывает полукруг, направленный выпуклой стороной вверх.
Подачу «веер» выполняют в правую сторону — слева направо,
тогда игрок занимает правостороннюю стойку, и в левую, когда теннисист становится лицом к столу.''')

        bot.send_message(message.chat.id, '3. Подача с обратным вращением.')
        bot.send_message(message.chat.id, '''Чтобы выполнить подачу с обратным вращением вам надо повернуть кисть в сторону вашего тела (во внутрь),
и угол вашего загиба должен быть большим, после броска мяча вам следует резким движением выпрямить кисть. 
Также мяч надо отбивать у правого бока вашего туловища.''')

    elif message.text == '3' and verification_pitch == True:

        bot.send_message(message.chat.id, '1. Топорик.')
        bot.send_message(message.chat.id, '''Перемещая ракетку вправо или влево, игрок придает мячу боковое вращение с вертикальной осью.
Стоит заметить, что не существует чистых видов вращения.
Каждый удар приводит к тому, что мяч начинает двигаться по траектории с верхне-боковым или нижне-боковым вращением.
При ударе ракеткой по мячу, мяч полетит влево или вправо, направление зависит от вращения.''')
        toporik = open('pictures/toporik.jpg', 'rb')
        bot.send_photo(message.chat.id, toporik)
        bot.send_message(message.chat.id, '''Выполняется движением сверху вниз, будто "срубаешь".
Во время удара спортсмен приседает. Топорик имеет как правило боковое-верхнее вращение.''')

        bot.send_message(message.chat.id, '2. Маятник, но с верхним вращением.')
        mayatnic = open('pictures/mayatnik.png', 'rb')
        bot.send_photo(message.chat.id, mayatnic)
        bot.send_message(message.chat.id, '''Выполняя эту подачу, ракетка движется справа на лево и мячу придается левое боковое вращение. 
Когда вы завершаете подачу сделайте движение вверх, чтобы придать мячу верхнее вращение.''')

bot.polling(none_stop=True)