from collections import deque

food_quantity=int(input())
orders=deque(map(int,input().split(' ')))

print(max(orders))

for r in range (len(orders)):
    order=orders.popleft()
    food_quantity=food_quantity-order
    if food_quantity<0:
        print('Orders left: ', end='')
        orders.appendleft(order)
        while orders:
            print(f'{orders.popleft()} ', end='')
        break

else:
    print('Orders complete')
