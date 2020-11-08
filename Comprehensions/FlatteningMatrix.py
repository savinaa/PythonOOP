
matrix=[[int(x) for x in input().split(', ')] for _ in range(int(input()))]
print([num for sublist in matrix for num in sublist])