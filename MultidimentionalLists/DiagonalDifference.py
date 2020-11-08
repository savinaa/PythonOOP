matrix_size=int(input())
matrix=[]
sum=0
for row in range(0,matrix_size):
    line=input().split(' ')
    matrix.append([j for j in line])
for i in range(matrix_size):
    num1=int(matrix[i][i])
    num2=int(matrix[i][matrix_size-1-i])
    sum+=num1-num2
print(abs(sum))