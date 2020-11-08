from itertools import combinations
names=input().split(',')
chairs=int(input())
results=combinations(names,chairs)
for result in results:
    print(",".join(result))
