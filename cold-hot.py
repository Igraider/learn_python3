import random

max_digits = 3
max_guess = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(max_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тепло')

    if len(clues) == 0:
        return 'Холодно'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

print('Я загадаю %s значное число, которое вы должны отгадать.' % (max_digits))
print('Я дам вам несколько подсказок...')
print('Когда я говорю:    Это означает:')
print('Холодно            Ни одна цифра не отгадана.')
print('Тепло              Одна цифра отгадана, но не отгадана ее позиция.')
print('Горячо             Одна цифра и ее позиция отгаданы.')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадал число. У вас %s попыток, чтобы его отгадать.' % (max_guess))
    guessTaken = 1
    while guessTaken <= max_guess:
        guess = ''
        while len(guess) != max_digits or not isOnlyDigits(guess):
            print('Попытка №%s' % (guessTaken))
            guess = input()
        print(getClues(guess, secretNum))
        guessTaken += 1

        if guess == secretNum:
            break
        if guessTaken > max_guess:
            print('Попыток большене осталось. Я загадал %s' % (secretNum))

    print('Хотите сыграть еще раз?')
    if not input().lower().startswith('д'):
        break
            