num=int(input())
matrix=[[col for col in input().split(', ')] for row in range(num)]
first_diagonal=[]
second_diagonal=[]
for row in range(num):
    first_diagonal.append(matrix[row][row])
    second_diagonal.append(matrix[row][num-1-row])
print(f'First diagonal: {", ".join(first_diagonal)}. Sum: {sum(int(n)for n in first_diagonal)}')
print(f'Second diagonal: {", ".join(second_diagonal)}. Sum: {sum(int(n)for n in second_diagonal)}')
