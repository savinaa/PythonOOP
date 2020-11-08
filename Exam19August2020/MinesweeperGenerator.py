size_matrix=int(input())
bombs=int(input())
matrix=[ [0 for i in range(size_matrix)]for j in range(size_matrix)]


def valid_indices(row, col):
    if row>=0 and row<size_matrix and col>=0 and col<size_matrix:
        if matrix[row][col]!='*':
            return True
        return False


for i in range(bombs):
    row,col=tuple(map(int,input().replace('(','').replace(')','').split(', ')))
    matrix[row][col]='*'
    if valid_indices(row-1,col-1):matrix[row-1][col-1]+=1
    if valid_indices(row-1,col):matrix[row-1][col]+=1
    if valid_indices(row-1,col+1):matrix[row-1][col+1]+=1

    if valid_indices(row,col-1):matrix[row][col-1]+=1
    if valid_indices(row,col+1):matrix[row][col+1]+=1

    if valid_indices(row+1,col+1):matrix[row+1][col+1]+=1
    if valid_indices(row+1,col):matrix[row+1][col]+=1
    if valid_indices(row+1,col-1):matrix[row+1][col-1]+=1

print('\n'.join([' '.join([item.__str__() for item in row])for row in matrix]))

