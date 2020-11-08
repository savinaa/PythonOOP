from itertools import product
from functools import reduce
numbers=input().split(', ')
n=len(numbers)
product=[list(x)for x in (product('+-',repeat=n))]
for sign in product:
    elements=[''.join(x)for x in list(zip(sign,numbers))]
    expression=''.join(elements)
    print(f'{expression}={eval(expression)}')