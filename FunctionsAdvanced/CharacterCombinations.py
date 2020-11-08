from itertools import permutations
string=input()
result=permutations(string)
for value in list(result):
    print("".join(value))
