num=int(input())
maxSet=set()

def populateSet(tuple):
    start, end = map(int,tuple.split(','))
    set1 = set()
    for i in range(start, end+1):
        set1.add(i)
    return set1

for i in range(num):
    tuple1,tuple2=input().split('-')
    set1 = populateSet(tuple1)
    set2 = populateSet(tuple2)
    result=set1.intersection(set2)
    if len(result)>len(maxSet):
        maxSet=result

print(f'Longest intersection is [{maxSet}] with length {len(maxSet)}'.replace('{','').replace('}',''))
