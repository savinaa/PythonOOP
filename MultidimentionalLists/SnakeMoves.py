from collections import deque
rows, cols=map(int,input().split(' '))
matrix=[ [ '0' for i in range(cols) ] for j in range(rows) ]
snake=deque(input())
for row in range(rows):
    if row%2==0:
        for col in range(cols):
            matrix[row][col]=snake.popleft()
            snake.append(matrix[row][col])
    else:
        for col in reversed(range(cols)):
            matrix[row][col] = snake.popleft()
            snake.append(matrix[row][col])
print('\n'.join([''.join([item for item in row]) for row in matrix]))
