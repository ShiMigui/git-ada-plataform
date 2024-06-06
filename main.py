from cases import getColumns, getColumnsKeys, getLine, getColumn, getLines, getLinesKeys
from re import sub
import grid
print('\tI love cats!\n')

currentPlayer = 'X'
board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def nextPlayer():
    global currentPlayer
    currentPlayer = 'X' if (currentPlayer == 'O') else 'O'

def cleanText(text):
    return sub(r'\s+', ' ', text.strip()).lower()

def convert(cmd=''):
    cmd = cleanText(cmd)
    arr = cmd.split(' ')

    if len(arr) != 2:
        raise ValueError("Invalid input. Please provide a line and a column.")

    if arr[0] in getLines() or arr[1] in getColumns():
        return [getLine(arr[0]), getColumn(arr[1])]
    else: return [getLine(arr[1]), getColumn(arr[0])]

def getSquare(yx=[]):
    return board[yx[0]][yx[1]]

def printBoard():
    print(grid.construct(board, '\t'))

def verifyBoard(board, currentPlayer):
    # Verificar linhas
    for row in board:
        if all([cell == currentPlayer for cell in row]):
            return True

    # Verificar colunas
    for col in range(len(board)):
        if all([board[row][col] == currentPlayer for row in range(len(board))]):
            return True

    # Verificar diagonal principal
    if all([board[i][i] == currentPlayer for i in range(len(board))]):
        return True

    # Verificar diagonal secundária
    if all([board[i][len(board) - 1 - i] == currentPlayer for i in range(len(board))]):
        return True

    return False

err=None
turn = 0
while(True):
    try:
        turn += 1
        if turn != 1:
            print("\n\n\n")

        print(f'\tTurn... {turn}')
        print(f'\tCurrent player... {currentPlayer}')
        print(f'\tLines... {getLinesKeys()} \n\tColumns... {getColumnsKeys()}\n')

        printBoard()
        
        if err:
            print(f'\t{err}')
            err = None

        cmd = input('\tCommand: ')

        [y, x] = yx = convert(cmd)

        square = getSquare(yx)
        if(square == ''):
            board[y][x] = currentPlayer
        else: raise ValueError(f'Square already is filled')

        if verifyBoard(board, currentPlayer):
            print("\n\n\n")
            printBoard()
            print(f"\tWINNER: {currentPlayer}")
            break

        nextPlayer()
    except ValueError as e:
        err = e