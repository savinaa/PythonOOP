string=input()
matrix_size=int(input())

matrix=[[x for x in input()] for _ in range(matrix_size)]
turns=int(input())
rows=matrix_size
cols=len(matrix[0])


def find_symbol(symbol):
    for row in range(0,rows):
        for col in range(0,cols):
            if matrix[row][col]==symbol:
                return row,col

def outside_border(row,col):
    return row >=rows or row <0 or col>=cols or col<0


player_pos=find_symbol('P')
player_row, player_col=player_pos
for i in range(turns):
    command=input()
    if command=='down':
        if outside_border(player_row+1,player_col):
            string=string[:-1]
        else:
            matrix[player_row][player_col] = '-'
            player_row=player_row+1
            if matrix[player_row][player_col]!='-':
                string+=matrix[player_row][player_col]
                matrix[player_row][player_col]='P'
    elif command=='up':
        if outside_border(player_row-1,player_col):
            string=string[:-1]
        else:
            matrix[player_row][player_col] = '-'
            player_row=player_row-1
            if matrix[player_row][player_col]!='-':
                string+=matrix[player_row][player_col]
                matrix[player_row][player_col]='P'
    elif command=='right':
        if outside_border(player_row,player_col+1):
            string=string[:-1]
        else:
            matrix[player_row][player_col] = '-'
            player_col=player_col+1
            if matrix[player_row][player_col]!='-':
                string+=matrix[player_row][player_col]
                matrix[player_row][player_col]='P'
    elif command=='left':
        if outside_border(player_row,player_col-1):
            string=string[:-1]
        else:
            matrix[player_row][player_col]='-'
            player_col=player_col-1
            if matrix[player_row][player_col]!='-':
                string+=matrix[player_row][player_col]
                matrix[player_row][player_col]='P'


print(string)
for row in matrix:
    print(''.join(row))