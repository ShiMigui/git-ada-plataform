def construct(board, it=''):
    text=''

    i = len(board)
    r = range(i)

    for x in r:
        text += f'{it}╔═══╦═══╦═══╗\n{it}' if x == 0 else f'{it}╠═══╬═══╬═══╣\n{it}'
        
        for y in r:
            v = board[x][y]

            if v == '':
                v = ' '
            
            text += f'║ {v} '

            if y == i - 1:
                text += '║\n' 

    text += f'{it}╚═══╩═══╩═══╝'    
    return text