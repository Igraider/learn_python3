import time
from sys import exit
from random import randint
import random


class Scene(object):

    def enter(self):
        pass

class Dead(Scene):

    deaths = ["Как можно было так погибнуть?",
        "Эх ты...",
        "Даже песик умнее...",
        "Бывает..."]

    def enter(self):
        time.sleep(1)
        print()
        print("Ты умер.")
        print(random.choice(Dead.deaths))
        exit(1)

class Engine(object):

    def __init__(self, some_scene):
        self.some_scene = some_scene

    def play(self):

        current_scene = self.some_scene.openning_scene()
        last_scene = self.some_scene.value_of_scene('finish')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.some_scene.value_of_scene(next_scene_name)

        current_scene.enter()

class Beginning(Scene):

    def enter(self):
        print("Ты очутился в темном подземелье...")
        time.sleep(2)
        print("Тебя ожидает небольшое приключение в котором ты проверишь свою удачу и находчивость.")
        time.sleep(3)
        print("Готов?")
        choice = input('> ')
        if choice == "да" or choice == "Да":
            return "crocodile"
        elif choice == "Нет" or choice == "нет":
            return "start"

class Crocodile_Room(Scene):

    def enter(self):
        print("Ты идешь...")
        time.sleep(2)
        print("И приходишь в какую - то комнату.")
        time.sleep(2)
        print("НЕ ПОНЯЛ! А где свет?!")
        time.sleep(1)
        print("Перед собой ты слышишь как что - то плещется в воде.")
        time.sleep(2)
        print("Ой!! Ты на что - то наступил.")
        time.sleep(2)
        print("Ты услышал действие какого - то механизма.")
        time.sleep(2)
        print("Что предпринять?")
        time.sleep(1)
        print("1. Cо всех ног побежать вперед.")
        print("2. Остаться на месте.")
        choice = input('> ')

        if choice == "1":
            print("Ты побежал вперед и провалился в бассейн с КРОКОДИЛАМИ!")
            time.sleep(3)
            return "dead"
        
        elif choice == "2":
            time.sleep(2)
            print ("Ты остался на месте и правильно сделал!")
            time.sleep(1)
            print("Включился свет! И закрылся бассейн с КРОКОДИЛАМИ!")
            time.sleep(2)
            print("Ты двинулся вперед...")
            input()
            return "killer"
        
        else:
            print("Не знаю что ты сделал, но это лучше чем бежать вперед.")
            print("Включился свет! И закрылся бассейн с КРОКОДИЛАМИ!")
            return "killer"

class Killer_Room(Scene):

    def enter(self):
        print("Ты заходишь в следущую комнату и видишь перед собой человека.")
        time.sleep(4)
        print("Он весь одет в измазанную кровью, темную одежду.")
        time.sleep(2)
        print("В руке нож!")
        time.sleep(1)
        print("Он говорит:\n Попрощайся с жизнью!")
        time.sleep(3)
        print("Что предримишь?")
        print("1. Попробовать пошутить.")
        print("2. Попробовать победить его.")
        print("3. Попробовать сбежать.")
        choice = input('> ')
        if choice == "1":
            print("Ты решил пошутить:")
            time.sleep(2)
            print("Если убить убийцу, количество убийц не изменится.")
            time.sleep(3)
            print("Он так смеялся, что решил оставить тебя в живых.")
            time.sleep(2)
            print("Ты пошел дальше...")
            input()
            return "cooker"

        elif choice == "2":
            print("Ты решил победить его:")
            print("Он ударил тебя ножом в живот")
            return "dead"

        elif choice == "3":
            print("Ты решил сбежать:")
            print("Он увидел это и перегородил тебе дорогу.")
            print("ТЕБЕ КОНЕЦ!")
            return "dead"

class Cooker_Room(Scene):

    def enter(self):
        dead_poison = randint(1, 3)
        if dead_poison == 1:
            tp_poison = randint(2, 3)
            if tp_poison == 2:
                next_level_poison = 3
            elif tp_poison == 3:
                next_level_poison = 2
        
        elif dead_poison == 2:
            tp_poison = random.choice([1,3])
            if tp_poison == 1:
                next_level_poison = 3
            elif tp_poison == 3:
                next_level_poison = 1

        elif dead_poison == 3:
            tp_poison = randint(1, 2)
            if tp_poison == 1:
                next_level_poison = 2
            elif tp_poison == 2:
                next_level_poison = 1

        print("Ты пришел и перед собой увидел на первый взгляд обычного повара.")
        time.sleep(3)
        print("Он сказал:")
        print("Не выпущу если не выпьешь мое фирменное зелье.")
        time.sleep(2)
        print("Выбирай:")
        print("1. Фиолетовое.")
        print("2. Синее.")
        print("3. Зеленое.")
        choice = int(input('> '))
        time.sleep(2)
        
        if choice == dead_poison:
            print("Ты выбрал смертельное зелье.")
            input()
            return "dead"

        elif choice == tp_poison:
            print("Ты заснул...")
            right_key = randint(1, len(list((Map.scenes).keys())))
            input()
            return str(keys[right_key-1])

        elif choice == next_level_poison:
            print("Это было хорошее зелье.")
            print("Ты пошел дальше...")
            return "sailer"
        
        else:
            print("Ты не захотел пить его зелье.")
            return 'dead'


class Sailer_Room(Scene):

    def enter(self):
        global fruit
        global gun
        print("Ты встретил человека полу-призрака, он спросил:")
        time.sleep(2)
        print("Что ты возьмешь с собой в дорогу?")
        time.sleep(2)
        print("1. Автомат.")
        print("2. Апельсин.")
        print("3. Яблоко")
        choice = input('> ')
        if choice == "1":
            print("Ты взял с собой автомат.")
            gun = True
            input()
            return "rabbit"

        elif choice == "2":
            print("Ты взял с собой апельсин.")
            fruit = True
            input()
            return "rabbit"

        elif choice == "3":
            print("Ты взял с собой яблоко.")
            fruit = True
            input()
            return "rabbit"

        else:
            print("Напиши цифру!")
            return "sailer"


class Rabbit_Room(Scene):

    def enter(self):
        global rabbit_kind
        print("В следующей комнате ты встретил КРОЛИКА-МУТАНТА с красными глазами!")
        time.sleep(2)
        if fruit == True:
            print("Варианты действий:")
            print("1. Попробовать пробежать в другую комнату.")
            print("2. Попробовать поговорить с ним.")
            print("3. Попробовать дать ему фрукт.")
            choice = input('> ')
            time.sleep(1)
            if choice == "1":
                time.sleep(1)
                print("Ты решил побежать в другую комнату.")
                time.sleep(2)
                print("Видно ты не учел его размеров.")
                return 'dead'
            elif choice == "2":
                time.sleep(1)
                print("Кролики-мутанты не разговариют, поэтому...")
                time.sleep(1)
                return "dead"
            elif choice == "3":
                print("Ты решил ему дать свой фрукт, ему он очень понравился.")
                print("Его глаза стали зелеными.")
                print("Он разрешил пройти дальше...")
                rabbit_kind = True
                input()
                return 'wall'

        elif gun == True:
            print("Варианты действий:")
            print("1. Попробовать пробежать в другую комнату.")
            print("2. Попробовать поговорить с ним.")
            print("3. Попробовать убить его из автомата.")
            choice2 = input("> ")
            time.sleep(1)
            if choice == "1":
                time.sleep(1)
                print("Ты решил побежать в другую комнату.")
                time.sleep(2)
                print("Видно ты не учел его размеров.")
                return 'dead'
            elif choice == "2":
                time.sleep(1)
                print("Кролики-мутанты не разговариют, поэтому...")
                time.sleep(1)
                return "dead"
            elif choice2 == "3":
                print("Ты решил убить его из автомата.")
                time.sleep(1)
                print("Как выяснилось ему не страшны пули, ты сделал его только злее...")
                input()
                return 'dead'
            
        else:
            print("Варианты действий:")
            print("1. Попробовать пробежать в другую комнату.")
            print("2. Попробовать поговорить с ним.")
            choice3 = input("> ")
            time.sleep(1)
            if choice3 == "1":
                time.sleep(1)
                print("Ты решил побежать в другую комнату.")
                time.sleep(2)
                print("Видно ты не учел его размеров.")
                return 'dead'
            elif choice3 == "2":
                time.sleep(1)
                print("Кролики-мутанты не разговариют, поэтому...")
                time.sleep(1)
                return "dead"
            else:
                print("Ты ничего не решил...")
                input()
                return "dead"




class Wall(Scene):

    def enter(self):
        waiting = 0
        def wait():
            print("Ты решил подождать.")
            while waiting != 5:
                print("Ничего не произошло.")
                waiting += 1
                print("Что будешь делать?")
                time.sleep(1)
                print()
                print("1. Подождать, вдруг расстает.")
                print("2. Попробовать разломать.")
                print("3. Вернуться к кролику.")
            print("К сожалению тебе очень хотелось есть")
            return "dead"
            
        def back_to_rabbit():
            input()
            print("Ты пошел к кролику.")
            time.sleep(1)
            print("Ты позвал его помочь разрушить стену")
            time.sleep(2)
            print("Он слегка ударил, и она разрушилась.")
            time.sleep(2)
            print("Ты сказал ему 'спасибо' и пошел дальше.")
            input()
            

        def bitting():
            print("Ты решил попробовать ее разбить.")
            time.sleep(2)
            print("Ты ударил по ледяной стене, и на тебя упала глыба...")
            input()

        print("В следующей комнате ты увидел ледяной барьер.")
        time.sleep(3)
        print("Что будешь делать?")
        time.sleep(1)
        if rabbit_kind == True:
            print("1. Подождать, вдруг расстает.")
            print("2. Попробовать разломать.")
            print("3. Вернуться к кролику.")
            choice = input("> ")
            if choice == "1":
                wait()
                choice2 = input("> ")
                if choice2 == "1":
                    print()
                elif choice2 == "2":
                    bitting()
                elif choice2 == "3":
                    print("Нажмите (Enter)")
                    back_to_rabbit()
                    
            elif choice == "2":
                bitting()
                return "dead"
            elif choice == "3":
                print("Нажмите (Enter)")
                back_to_rabbit()
                return "chest"
        else:
            print("1. Подождать, вдруг расстает.")
            print("2. Попробовать разломать.")
            choice = input("> ")
            if choice == "1":
                wait()
                
            elif choice == "2":
                bitting()
                return 'dead'
class Chest(Scene):

    def enter(self):
        def opening():
            time.sleep(1)
            print("Ты начал открывать его как вдруг,")
            time.sleep(2)
            print("Cундук открылся, и высунулась большая пасть!")
            time.sleep(2)
            print("Это был мимик!")
            
        time.sleep(1)
        print("В этой комнате стоял золотой сундук.")
        print("Что делать?")
        print("1. Поискать к нему ключ.")
        print("2. Пойти в следующую комнату.")
        print("3. Попробовать открыть его...")
        choice = input("> ")
        if choice == "1":
            time.sleep(3)
            print("Ты ничего не нашел.")
            time.sleep(1)
            print("Что делать?")
            time.sleep(1)
            print("1. Пойти в следующую комнату.")
            print("2. Попробовать открыть его...") 
            choice2 = input("> ")
            if choice2 == "1":
                return "boss"
            elif choice2 == "2":
                opening()
                return "dead"
        elif choice == "2":
            return "boss"
        elif choice == "3":
            opening()  

            
class BOSS(Scene):

    def enter(self):
        print()

class Map(object):

    scenes = {
        "crocodile" : Crocodile_Room(),
        "start" : Beginning(),
        "killer" :  Killer_Room(),
        "cooker" : Cooker_Room(),
        "sailer" : Sailer_Room(),
        "rabbit" : Rabbit_Room(),
        "wall" : Wall(),
        "chest" : Chest(),
        "boss" : BOSS(),
        "dead" : Dead()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def value_of_scene (self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def openning_scene(self):
        return self.value_of_scene(self.start_scene)

gun = False
fruit = False
rabbit_kind = False

a_map = Map("wall")
a_game = Engine(a_map)
a_game.play()