command=input()
numbers=list(map(int,input().split(' ')))
len_numbers=len(numbers)
resulted_list=[]
if command=='Odd':
    resulted_list=list(filter(lambda x: x%2!=0,numbers))
else:
    resulted_list = list(filter(lambda x: x % 2 == 0, numbers))
print(f'{sum(resulted_list)*len_numbers}')