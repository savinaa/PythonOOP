rows, cols=map(int,input().split(' '))
matrix=[]
for row in range(rows):
    line=input().split(' ')
    matrix.append([j for j in line])
square_count=0
for row in range(rows):
    for col in range(cols):
        try:
            if matrix[row][col]==matrix[row][col+1] \
            and matrix[row][col+1]==matrix[row+1][col]\
            and matrix[row][col+1]==matrix[row+1][col+1]:
                square_count+=1
        except:
            continue
print(square_count)
