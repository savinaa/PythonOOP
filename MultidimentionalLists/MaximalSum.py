rows, cols=map(int,input().split(' '))
max_sum=-999999
best_indices=0,0
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
for row in range(rows-2):
    for col in range(cols-2):
        sum=matrix[row][col]+matrix[row][col+1]+matrix[row][col+2]\
        + matrix[row+1][col]+matrix[row+1][col+1]+matrix[row+1][col+2]\
        +matrix[row+2][col]+matrix[row+2][col+1]+matrix[row+2][col+2]
        if sum>max_sum:
            max_sum=sum
            best_indices=row,col
little_matrix= [[0 for i in range(3)]for j in range(3)]
best_row,best_col=best_indices
for row in range(3):
    for col in range(3):
        little_matrix[row][col]=matrix[best_row+row][best_col+col]
print(f'Sum = {max_sum}')
print('\n'.join([' '.join([item.__str__() for item in row])for row in little_matrix]))
