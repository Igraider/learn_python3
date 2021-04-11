async def on_message(message):
    global comments
    
    msg = message.content.lower()

    hello_words = ['Привет', 'привет', 'дароу', 'Дароу', 'Hello', 'hello', 'Hi', 'hi',
    'Хелоу', 'хелоу', 'Дарова', 'дарова', 'Приветики', 'приветики', 'HI']

    goodbye_words = ['пока', 'goodbye','bb', 'до свидания', 'свидания']

    bad_words = ['бля', 'blya','хуй','хуи','хуя','нах','хуе','хул','hui','xuy','xui','xy','xy','хе','her','xep','xer','еба','еби','иба','eba','iba','ebi','e6u','ebu','e6i','ебло','eblo','e6y','муда','муде','муди','muda','muga','mude','muge','mudi','mugi','mudu','mugu','манд','mand','mang','mahg','пида','пидо','пидр','nuga','nugo','nugp','pida','pido','pidr','пизд','pizd','nu3d','pi3d','сука','suka','gandon','гандон','rangon','gondon','гондон','rongon'	,'ept','епт','wmara','shmara','шмара','pedik','педик'	,'neduk','lowar','loshar','лошар','лох','loh','tvar','тварь','tbap','чмо','chmo','епал','epal','enal','debil','dibil','дибил','дебил','дэбил','дурок','durok','pri','дурень','duren','дурак','durak','даун','daun','шлюха','писька','dick',
    'shluha','долбаеб','долбаёб','падла','шалава','идиот','idiot','autist','аутист', 'говно','govno', 'говна', 'даyн','мать в канаве', 'курва','долбоеб','gey','gay','gai','gei','гей','гeй','gomosek','гомосек','gomosec','gеi']
    
    if msg in bad_words:
        await message.channel.purge(limit=1)
        await message.channel.send("Не ругайся!")
        time.sleep(1)
        await message.channel.purge(limit=1)
    if msg in goodbye_words:
            await message.channel.send("Пока, удачи тебе!")
    if msg in hello_words:
        await message.channel.send("Привет друг!")
    if message.content:
        comments += 1
    if comments == 20:
        comments = 0
        emb = discord.Embed(title=f'Вам нравиться сервер?',
        description='',
        colour=discord.Color.green())

        message = await message.channel.send(embed=emb) # Возвращаем сообщение после отправки
        await message.add_reaction('✅')
        await message.add_reaction('❌')