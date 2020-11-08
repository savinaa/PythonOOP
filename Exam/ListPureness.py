from collections import deque
from sys import maxsize
def best_list_pureness(*args):
    list,rotations=args
    listing=deque(list)
    indices=[]
    for i in range(len(listing)):
        indices.append(i)
    highest_pureness=0
    high_pur_index=0
    index=0
    for rotation in range(len(list)):
        curr_rot= listing
        zipped_data=zip(curr_rot,indices)
        local_sum=0
        for item in zipped_data:
            value,ind=item
            local_sum+=value*ind
        if local_sum>highest_pureness:
            highest_pureness=local_sum
            high_pur_index=index
        index+=1
        value=listing.pop()
        listing.appendleft(value)
        if rotation==rotations:
            break
    result=format(f'Best pureness {highest_pureness} after {high_pur_index} rotations')
    return result

test = ([1,2,3,4,5,6,7,8,9], 0)
result = best_list_pureness(*test)
print(result)




