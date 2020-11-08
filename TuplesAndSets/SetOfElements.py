m,n=tuple(map(int, input().split(' ')))

set1=set()
set2=set()

for i in range(m):
    number=input()
    set1.add(number)

for i in range(n):
    number=input()
    set2.add(number)

result=set1.intersection(set2)
for i in result:
    print(i)
