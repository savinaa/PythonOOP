import itertools
dimensions=int(input())
matrix=[[int(col) for col in input().split(' ')] for row in range(dimensions)]
while True:
    token=input().split(' ')
    if len(token)==1:
        break
    command=token[0]
    row=int(token[1])
    column=int(token[2])
    value=int(token[3])
    if row<0 or row>dimensions-1 or column<0 or column>dimensions-1:
        print("Invalid coordinates")
        continue
    if command=="Add":
        matrix[row][column]+=value
    elif command=="Subtract":
        matrix[row][column]-=value
print('\n'.join([' '.join([item.__str__() for item in row]) for row in matrix]))