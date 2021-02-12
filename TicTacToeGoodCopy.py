# Tic Tac Toe By Gurjot kooner
import time
import os
import random

def drawBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Want to play another? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter) or
    (board[7] == letter and board[5] == letter and board[3] == letter) or
    (board[9] == letter and board[5] == letter and board[1] == letter))

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)(Bottom left to top right)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("""  


 .----------------.  .----------------.  .----------------.            .----------------.  .----------------.  .----------------.            .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |          | .--------------. || .--------------. || .--------------. |          | .--------------. || .--------------. || .--------------. |
| |  _________   | || |     _____    | || |     ______   | |          | |  _________   | || |      __      | || |     ______   | |          | |  _________   | || |     ____     | || |  _________   | |
| | |  _   _  |  | || |    |_   _|   | || |   .' ___  |  | |          | | |  _   _  |  | || |     /  \     | || |   .' ___  |  | |          | | |  _   _  |  | || |   .'    `.   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |      | |     | || |  / .'   \_|  | |  ______  | | |_/ | | \_|  | || |    / /\ \    | || |  / .'   \_|  | |  ______  | | |_/ | | \_|  | || |  /  .--.  \  | || |   | |_  \_|  | |
| |     | |      | || |      | |     | || |  | |         | | |______| | |     | |      | || |   / ____ \   | || |  | |         | | |______| | |     | |      | || |  | |    | |  | || |   |  _|  _   | |
| |    _| |_     | || |     _| |_    | || |  \ `.___.'\  | |          | |    _| |_     | || | _/ /    \ \_ | || |  \ `.___.'\  | |          | |    _| |_     | || |  \  `--'  /  | || |  _| |___/ |  | |
| |   |_____|    | || |    |_____|   | || |   `._____.'  | |          | |   |_____|    | || ||____|  |____|| || |   `._____.'  | |          | |   |_____|    | || |   `.____.'   | || | |_________|  | |
| |              | || |              | || |              | |          | |              | || |              | || |              | |          | |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |          | '--------------' || '--------------' || '--------------' |          | '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'           '----------------'  '----------------'  '----------------'            '----------------'  '----------------'  '----------------' 

                                                                            To win get three in a row
                                                                                 
                                                                                 !!!!IMPORTANT!!!!
                                                                                 
                           Each Box is numbered from 1-9 starting from the BOTTOM left to TOP right, You have to enter a number from 1-9 to specify your choice
                                                                  The computer will choose who goes first randomly
""")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('You have tied the game!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You have lost the game')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('You have tied the game!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break