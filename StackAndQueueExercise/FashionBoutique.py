clothes=list(map(int,input().split(' ')))
rack_size=int(input())

current_rack_size=rack_size
racks_counter=0
while clothes:
    outfit=clothes.pop()
    remaining_rack_space = current_rack_size - outfit
    if remaining_rack_space >0:
        current_rack_size= remaining_rack_space
    elif remaining_rack_space ==0:
        racks_counter=racks_counter+1
        current_rack_size = rack_size
    else:
        racks_counter = racks_counter + 1
        current_rack_size = rack_size
        clothes.append(outfit)

if current_rack_size>0 and current_rack_size!=rack_size:
    racks_counter=racks_counter+1

print(racks_counter)
