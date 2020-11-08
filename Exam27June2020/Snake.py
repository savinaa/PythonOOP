matrix_size=int(input())
matrix= [ [ i for i in input() ] for j in range(0,matrix_size) ]


def find_symbol(symbol):
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col]==symbol:
                return row,col


#initial snake position
current_snake_pos:tuple=find_symbol('S')

eaten_food=0



def move(row,col):
    curr_row,curr_col=current_snake_pos
    return curr_row+row,curr_col+col

snake_dead=False


def invalid_index(curr_row, curr_col):
    return curr_row<0 or curr_row>matrix_size-1 or curr_col<0 or curr_col>matrix_size-1


while True:
    if eaten_food==10:
        break
    command=input()
    curr_row, curr_col = tuple(current_snake_pos)
    matrix[curr_row][curr_col]='.'
    if command=='up':
        curr_row, curr_col=move(-1,0)
    elif command=='down':
        curr_row, curr_col = move(1,0)
    elif command=='left':
        curr_row, curr_col = move(0,-1)
    elif command=='right':
        curr_row, curr_col = move(0,1)

    if invalid_index(curr_row, curr_col):
        snake_dead = True
        break
    elif matrix[curr_row][curr_col] == 'B':
        matrix[curr_row][curr_col] = '.'
        curr_row, curr_col = find_symbol('B')
        matrix[curr_row][curr_col] = 'S'
    else:
        if matrix[curr_row][curr_col] == '*':
            eaten_food += 1

    matrix[curr_row][curr_col] = 'S'
    current_snake_pos = curr_row, curr_col

if eaten_food==10:
    print(f'You won! You fed the snake.')
else:
    print(f'Game over!')

print(f'Food eaten: {eaten_food}')

print('\n'.join([''.join([item for item in row]) for row in matrix]))