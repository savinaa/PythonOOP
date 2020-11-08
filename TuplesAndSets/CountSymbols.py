import collections

string=sorted(input())
dict =collections.defaultdict(int)

for s in string:
    dict[s]+=1

for key,value in dict.items():
    print(f'{key}: {value} time/s')