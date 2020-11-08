from collections import deque

rows,cols=list(map(int, input().split(' ')))
matrix=[[0 for x in range(cols)] for y in range(rows)]
player_row, player_col=-1,-1
new_row, new_col=-1,-1

def populateRabbits():
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]=='B':
                try:
                    matrix[row-1][col] = 'B'
                    matrix[row+1][col] = 'B'
                    matrix[row][col-1] = 'B'
                    matrix[row][col+1] = 'B'
                except:
                    continue
    return matrix

def printMatrix():
    for row in matrix:
        print(''.join(row))

for row in range(rows):
    entry=input()
    matrix.append(x for x in entry)
    if 'P' in entry:
        player_row,player_col=row,entry.index('P')

new_row, new_col=-1,-1
commands=deque(list(input()))
while commands:
    command=commands.popleft()
    if command=='U':
        new_row,new_col=player_row-1,player_col
    elif command=='D':
        new_row, new_col = player_row + 1, player_col
    elif command == 'L':
        new_row, new_col = player_row, player_col-1
    elif command == 'D':
        new_row, new_col = player_row, player_col + 1

    try:
        matrix[player_row][player_col] = '.'
        if matrix[new_row][new_col]!='B':
            player_row, player_col = new_row, new_col
            matrix[player_row][player_col]='P'
            matrix=populateRabbits()
            if matrix[player_row][player_col]=='B':
                printMatrix()
                print(f'lost {player_row} {player_col}')
                break
        else:
            printMatrix()
            matrix = populateRabbits()
            print(f'lost {new_row} {new_col}')
            break
    except:
        matrix = populateRabbits()
        printMatrix()
        print(f'won {player_row} {player_col}')
        break
