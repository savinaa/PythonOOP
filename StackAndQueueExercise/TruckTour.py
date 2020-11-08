from collections import deque

pump_count=int(input())
stack=[]

for r in range(pump_count):
    pump_properties=list(map(int,input().split(' ')))
    pump_dist=pump_properties[0]-pump_properties[1]
    stack.append(pump_dist)

pump_index=0

current = 0
position = 0

for r in range(0,pump_count-1):
    current =stack[r]+current
    if (current < 0):
        current = 0
        position = r + 1

print(position)