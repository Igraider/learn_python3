import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = """аист акула мандарин ластик ручка мышка эпилепсия свет лампа стол окно аквариум кровать
яблоко апельсин конфета пылесос компьютер стекло лист футбол провод губка вентилятор рыба чайник часы клавиатура 
учебник утка перо петух хлеб история икра карандаш буква пластик загрязнение воздух кнопка шоколад картина запах загадка
пот хруст хрен ящик рюкзак песня музыка машина колесо мыло торт ананас котлета макароны пчела заяц лиса волк муравей""".split()

def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex]

def displayBoard(missed_letters, correct_letters, secretWord):
    global blanks
    print(HANGMANPICS[len(missed_letters)])
    print()

    print("Неправильные буквы: ", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()
    
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correct_letters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    print("Угаданные буквы: ", end=' ')    
    for letter in blanks:
        print(letter, end=' ')
    print()
def getGuess(already_guessed):
    while True:
        print("Введите букву.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Введите только одну букву.")
        elif guess in already_guessed:
            print("Вы уже называли эту букву. Введите другую.")
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print("Введите РУССКУЮ БУКВУ.")
        else:
            return guess

def playAgain():
    print("Хотите сыграть еще раз?")
    return input().lower().startswith("д")


print("В И С Е Л И Ц А")
missed_letters = ''
correct_letters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missed_letters, correct_letters, secretWord)

    guess = getGuess(missed_letters + correct_letters)

    if guess in secretWord:
        correct_letters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correct_letters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print("Ты угадал, это: '" + secretWord +"'")
            gameIsDone = True

    else:
        missed_letters += guess
    
        if len(missed_letters) == len(HANGMANPICS) - 1:
            print("Вы проиграли! Количество попыток закончилось! Секретное слово: " + secretWord)
            displayBoard(missed_letters, correct_letters, secretWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missed_letters = ''
            correct_letters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else: 
            break