n=int(input())
evens=set()
odd=set()
for index in range(n):
    name=input()
    askiiSum=0
    for i in name:
        askiiSum+=ord(i)

    askiiSum=askiiSum//(index+1)
    if askiiSum%2==0:
        evens.add(askiiSum)
    else:
        odd.add(askiiSum)
totalOddSum=sum(odd)
totalEvenSum=sum(evens)
if totalEvenSum==totalOddSum:
    result=odd.union(evens)
elif totalEvenSum>totalOddSum:
    result = odd.symmetric_difference(evens)
else:
    result=odd.difference(evens)

resultStr = ', '.join(list(map(str,result)))
print(resultStr)