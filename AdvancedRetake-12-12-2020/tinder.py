from collections import deque
def check_if_empty(deq):
    return len(deq) == 0

def divisibleBy25(n):
    return n%25==0

males = list(map(int,input().split(' ')))
females = list(map(int,input().split(' ')))
count_of_matches=0
while (True):
    males=deque(filter(lambda x:x>0,males))
    females=deque(filter(lambda x:x>0,females))
    if check_if_empty(males) or check_if_empty(females):
        break

    man=males.pop()
    woman=females.popleft()

    if divisibleBy25(man):
        females.appendleft(woman)
        if check_if_empty(males):
            break
        man = males.pop()
        continue

    if divisibleBy25(woman):
        males.append(man)
        if check_if_empty(females):
            break
        woman = females.popleft()
        continue

    if man==woman:
        count_of_matches+=1
    else:
        man=max(man-2,0)
        males.append(man)


print(f'Matches: {count_of_matches}')
if len(males)==0:
    print(f'Males left: none')
else:
    print(f'Males left: {", ".join([str(m) for m in reversed(males)])}')

if len(females) == 0:
    print(f'Females left: none')
else:
    print(f'Females left: {", ".join([str(f) for f in females])}')
