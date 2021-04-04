import discord
comments = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global comments
        # don't respond to ourselves
        if message.author == self.user:
            return

        hello_words = ['Привет', 'привет', 'дароу', 'Дароу', 'Hello', 'hello', 'Hi', 'hi',
        'Хелоу', 'хелоу', 'Дарова', 'дарова', 'Приветики', 'приветики', 'HI']

        goodbye_words = ['Пока', 'пока', 'гг', 'Гг', 'ГГ', 'Goodbye', 'goodbye', 'GOODBYE',
        'GG', 'gg', 'Gg', 'BB', 'bb']

        bad_words = ['бля, blya,хуй	,хуи,хуя,хуе,хул,hui,xuy,xui,xy,xy,хе,her,xep,xer,еба,еби,иба,eba,iba,ebi,e6u,ebu,e6i,ебло,eblo,e6y,муда,муде,муди,muda,muga,mude,muge,mudi,mugi,mudu,mugu,манд,mand,mang,mahg,пида,пидо,пидр,nuga,nugo,nugp,pida,pido,pidr,пизд,pizd,nu3d,pi3d,сука,suka,gandon,гандон,rangon,gondon,гондон,rongon	,ept,епт,wmara,shmara,шмара,pedik,педик	,neduk,lowar,loshar,лошар,лох,loh,tvar,тварь,tbap,чмо,chmo,епал,epal,enal,debil,dibil,дибил,дебил,дэбил,дурок,durok,pri,дурень,duren,дурак,durak']

        if message.content in bad_words:
            await message.channel.send("Не ругайся!")
            await message.channel.purge(limit=1)
        elif message.content in goodbye_words:
            await message.channel.send("Пока, удачи тебе!")
        elif message.content in hello_words:
            await message.channel.send("Привет друг!")

        if message.content:
            comments += 1
        if comments == 30:
            emb = discord.Embed(title=f'Вам нравиться сервер?',
            description='',
            colour=discord.Color.green())

            message = await message.channel.send(embed=emb) # Возвращаем сообщение после отправки
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            
        
    
client = MyClient()
client.run('ODI3OTMzMzE4ODg4MDMwMjI5.YGiO_Q.clOg0OHVeWY-DddDB5AjCpoxMIw')