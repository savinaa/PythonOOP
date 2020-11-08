import collections

d=collections.defaultdict(int)
values=tuple(map(float, input().split(' ')))
for i in values:
    d[i]+=1
for key,value in d.items():
    print(f'{key} - {value} times')
