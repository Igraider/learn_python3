import random

def display_board(board):

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Вы выбираете X или O?')
        letter = input().upper()
    
    if letter == 'X':
        return['X', 'O']
    elif letter == 'O':
        return['O', 'X']

def whoGoesFirst():

    if random.randint(0, 1):
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board, letter, move):
    board[move] = letter

def chooseRandomMoveFromList(board, moveList):
    possible_moves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possible_moves.append(i)
    
    if possible_moves != 0:
        return random.choice(possible_moves)

    else:
        return None

def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[1] == le and bo[4] == le and bo[7] == le) or 
    (bo[2] == le and bo[5] == le and bo[8] == le) or 
    (bo[3] == le and bo[6] == le and bo[9] == le) or 
    (bo[1] == le and bo[5] == le and bo[9] == le) or 
    (bo[3] == le and bo[5] == le and bo[7] == le))
    
def getBoardCopy(board):

    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy

def isSpaceFree(board, move):
     
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш следующий ход?')
        move = input()
    return int(move)

def getComputerMove(board, computer_letter):
    
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    
    for i in range(1, 10):
        board_copy = getBoardCopy(board)
        if isSpaceFree(board_copy, i):
            makeMove(board_copy, computer_letter, i)
            if isWinner(board_copy, computer_letter):
                return i

    for i in range(1, 10):
        board_copy = getBoardCopy(board)
        if isSpaceFree(board_copy, i):
            makeMove(board_copy, player_letter, i)
            if isWinner(board_copy, player_letter):
                return i

        
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    
    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2,4,6,8])

def isboardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False

    return True

print()
print('КРЕСТИКИ-НОЛИКИ')

while True:
    theBoard = [' '] * 10
    player_letter, computer_letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Человек':
            display_board(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, player_letter, move)   
        
            if isWinner(theBoard, player_letter):
                display_board(theBoard)
                print('Ты победил! Ура!')
                gameIsPlaying = False
            else:
                if isboardFull(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'
            
        else: 
            move = getComputerMove(theBoard, computer_letter)
            makeMove(theBoard, computer_letter, move)

            if isWinner(theBoard, computer_letter):
                display_board(theBoard)
                print('Компьютер победил! Вы проиграли.')
                gameIsPlaying = False
            else:
                if isboardFull(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Человек'
    print('Сыграем еще раз?')
    if not input().lower().startswith('д'):
        break    