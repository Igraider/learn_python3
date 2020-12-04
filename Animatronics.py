import time
from sys import exit
import pyglet

class scene(object):

    def enter(self):
        pass

class your_room(object):

    def enter(self):
        print()
        print("Похоже я уснул. Уже почти полночь.")
        time.sleep(3)
        print("*Звук падения металла*")
        song.play()
        time.sleep(1)
        print("Что это такое?")
        time.sleep(2)
        print("Странно, кроме меня здесь никого не должно быть.")
        time.sleep(3)
        print("Схожу проверю.")
        time.sleep(2)
        print("*Выключился свет*")
        time.sleep(2)
        print("Черт возьми! Что это было?")
        print("Нужно дойти до щитка в диспетчерской.")
        time.sleep(4)
        print("1. Пойти в диспетчерскую...")
        print("2. Остаться в кабинете.")
        choice = input('> ')
        if choice == "1":
            time.sleep(1)
            print("Пойду в диспетчерскую, незачем тут сидеть...")
            return 'light'
        elif choice == "2":
            print("Останусь здесь...")
            return 'death'
        else:
            print("Нормально напиши!")
            return 'room'

        

class engine(object):
    
    def __init__(self,some_scene):
        self.some_scene = some_scene

    def play(self):
        current_scene = self.some_scene.opening_scene()
        last_scene = self.some_scene.value_of_scene('finish')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.some_scene.value_of_scene(next_scene_name)

        current_scene.enter()
        

class off_light(scene):

    def enter(self):
        print("Так сюда, температура 23 градуса неплохо вполне себе комфортно.")
        time.sleep(2)
        print("Приёмник, какие - то бумажки, телефоны, пусто. Так где - то здесь, а вот хорошо...")
        input()
        print("А-А-А-А-А-А-А!!!! Тебя сьел аниматроник...")
        input()
        return 'room2'

class your_room2(scene):

    def enter(self):
        print("Приснится же такое!")
        print("Уже полночь. Пора идти домой.")
        input()
        return 'call'

class off_light2(scene):

    def enter(self):
        time.sleep(2)
        print("Что со светом? Кажется у меня дежавю?")
        time.sleep(2)
        print("Надо бы сходить проверить щиток в диспетчерской.")
        print("1. Пойти в диспетчерскую...")
        print("2. Остаться здесь...")
        choice = input('> ')
        if choice == "1":
            time.sleep(4)
            print("Так пришел, осталось найти электрический щит.")
            time.sleep(2)
            print("А вот и он.")
            time.sleep(1)
            print('Так - то лучше')
            time.sleep(2)
            print("*Дзынь* - *Дзынь*")
            time.sleep(2)
            print("**На этот раз телефон стоял на столе, напротив стола была решетка (для допросов)")
            time.sleep(4)
            print("Голос из телефона:")
            print("Ну, что вспомнил что - нибудь")
            time.sleep(2)
            print("Как тебе мой подарок?")
            time.sleep(1)
            print("За решеткой в темноте ты увидел две, как лазеры точки, ЭТО БЫЛ АНИМАТРОНИК!")
            time.sleep(2)
            print("Он скрылся в темноте.")
            print("Что предпринять?")
            print("1. Побежать в свою комнату.")
            print("2. Побежать в душевую.")
            choice2 = input('> ')
            if choice2 == "1":
                print("Ты побежал в свою комнату")
                time.sleep(2)
                print("Где спрятаться?")
                print("1. Под столом.")
                print("2. За дверью.")
                choice3 = input('> ')
                if choice3 == "1":
                    time.sleep(2)
                    print("Ты спрятался под столом.")
                    print("Аниматроник вбегает закрывает дверь и все осмаривает")
                    print("Ты сидел тихо, но он тебя заметил...")
                    return 'death'
                
                elif choice3 == "2":
                    time.sleep(1)
                    print("Ты спрятался за дверью.")
                    time.sleep(2)
                    print("Аниматроник вбегает закрыл дверь и увидел тебя")
                    time.sleep(1)
                    print("Ты попытался резко убежать,")
                    time.sleep(2)
                    print("Но он тебя поймал.")
                    return 'death'

            
            elif choice2 == "2":
                print("Ты побежал в душевую")
                time.sleep(1)
                return 'bathroom'
               
                
        elif choice == "2":
                print("Лучше в комнате посижу.")
                return 'death'

        else:
            print("Ты не смог решиться...")
            return 'death'


class calling(scene):

    def enter(self):
        print("*Дзынь* - *Дзынь*")
        print("Ночной вызов. Надеюсь обойдется без выездов.")
        time.sleep(1)
        print("Голос из телефона: Привет Бишоп.")
        time.sleep(2)
        print("Прекрасная ночь? Не правда ли?")
        time.sleep(2)
        print("Я уверен ты не помнишь меня.")
        time.sleep(2)
        print("Прошло много времени с момента нашей последней встречи...")
        time.sleep(2)
        print("Однажды, ты забрал все что у меня было, пришло время платить по счетам.")
        time.sleep(3)
        print("Бишоп: Что за псих?")
        time.sleep(2)
        print("*Выключился свет*")
        return 'light2'

class Bathroom(scene):
    
    def enter(self):
        print("Вбежав в душевую,")
        time.sleep(1)
        print("Ты увидел шкафчики и проход дальше (Видно там кабинки).")
        time.sleep(2)
        print("Куда спрятаться?")
        print("1. Шкафчик.")
        print("2. Кабинка.")

        choice = input('> ')
        if choice == "1":
            time.sleep(1)
            print("Ты спрятался в шкафчик.")
            time.sleep(2)
            print("Аниматроник вбегает и бежит в душевые, т.к он не нашел тебя он побежал в другую комнату.")
            time.sleep(3)
            print("Он что - то потерял, это карточка от склада, а на складе есть ключ ко всем дверям! Я сбегу отсюда.")
            input()
            return 'key'

        elif choice == "2":
            time.sleep(1)
            print("Ты спрятался в душевую кабинку.")
            time.sleep(1)
            print("Аниматроник бежит к душевым кабинкам")
            time.sleep(2)
            print("Он увидел тебя...")
            time.sleep(1)
            return 'death'

        else:
            print("Ты так и не решился...")
            time.sleep(1)
            return 'death'


class storage(scene):

    def enter(self):
        print("Ты тихо прибежал на склад.")
        print("Где же эта карта?")
        time.sleep(5)
        print("Фух, нашел.")
        time.sleep(1)
        print("Рядом с тобой была большая клетка с большой коробкой, которая все время гремела.")
        time.sleep(4)
        print("Странно...")
        print("Ты начинаешь отсюда бежать.")
        time.sleep(2)
        print("Эта коробка резко раскрывается и из нее вылезает ЕЩЕ ОДИН АНИМАТРОНИК!")
        time.sleep(2)
        print("Ты побежал к выходу.")
        input()
        return 'exit'


class blockage(scene):

    def enter(self):
        print("Ты уже у выхода, но из вентиляции выпрыгнул первый аниматроник и загородил тебе дорогу")
        input()
        print("Есть еще один выход!")
        print("Ты разворачиваешься назад и перед тобой другой аниматроник")
        time.sleep(4)
        print("1. Обойти его с левой стороны.")
        print("2. Обойти его с правой стороны.")
        print("3. Прыгнуть между ног.")
        choice = input('> ')
        if choice == "1":
            print("Он был готов к тому, что ты побежишь в сторону выхода...") 
            time.sleep(1)
            return 'death'

        elif choice == "2":
            print("Ты его обхитрил! Ты побежал в правую сторону, а затем в сторону второго выхода... ")
            return 'exit2'

        elif choice == "3":
            print("Ты попытался прыгнуть между ног, но он схватил тебя за шиворот...")
            time.sleep(2)
            return 'death'
            
        else:
            print("Ты так и не решился!")
            return 'death'


class maze(scene):

    def enter(self):
        print("И вот ты бежишь, перед тобой развилка:")
        time.sleep(1)
        print("1. Влево")
        print("2. Вправо")

        choice = input('> ')
        if choice == "1":
            time.sleep(2)
            print("Ты бежишь и тут...")
            time.sleep(2)
            print("Тупик...")
            time.sleep(2)
            return 'death'

        elif choice == "2":
            print("Ты бежишь и тут...")
            time.sleep(2)
            print("Еще одна развилка! Черт!")
            print("1. Влево")
            print("2. Вправо")
            choice2 = input('> ')
            if choice2 == "1":
                print("Ты сворачиваешь налево и тут...")
                time.sleep(2)
                print("Тупик...")
                return 'death'

            elif choice2 == "2":
                print("Ты сворачиваешь направо и тут...")
                time.sleep(2)
                print("Выход!!!")
                time.sleep(1)
                print("Ты открываешь дверь и захлопываешь ее за собой.")
                return 'finish'
                

class finished(scene):

    def enter(self):
        print("""
        
        
                                ТЫ ПОБЕДИЛ!!!
                                ПОЗДРАВЛЯЮ!!!                      
                                
                                """)

class Dead(scene):

    def enter(self):
        print()
        print("Тебя съели аниматроники...")
        print("Ты проиграл.")
        exit(1)

class map(object):

    scenes = {'room' : your_room(),
    'light': off_light(),
    'room2': your_room2(),
    'light2': off_light2(),
    'call': calling(),
    'bathroom': Bathroom(),
    'key': storage(),
    'exit': blockage(),
    'exit2': maze(),
    'death': Dead(),
    'finish': finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def value_of_scene(self, scene_name):
        val = map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.value_of_scene(self.start_scene)

song = pyglet.media.load("C:\\Users\\Ната\\Downloads\\Sound_03093.mp3")
pyglet.app.run
a_map = map('room')
a_game = engine(a_map)
a_game.play()