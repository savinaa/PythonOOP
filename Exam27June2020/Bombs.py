from collections import deque,defaultdict
bomb_effects=deque(map(int,input().split(', ')))
bomb_casings=deque(map(int,input().split(', ')))

created_bombs_effects=[]

bombs={
    'DATURA':40,
    'CHERRY':60,
    'SMOKE_DECOY':120,
}


created_bombs_effects=[]
unique_bombs=set()
created_bombs=defaultdict(int)


def all_bombs_created():
    return created_bombs['DATURA']>=3 and created_bombs['CHERRY']>=3 and created_bombs['SMOKE_DECOY']>=3


while True:
    if len(bomb_effects)==0 or len(bomb_casings)==0 or all_bombs_created() \
            or (len(bomb_effects)==1 and bomb_effects[0]<=0):
        break
    bomb=bomb_effects.popleft()
    casing=bomb_casings.pop()
    power=bomb+casing
    if power in bombs.values():
        created_bomb=[bomb_name for bomb_name,bomb_power in bombs.items() if power==bomb_power]
       # created_bombs_effects.append( bomb)
        unique_bombs.add(created_bomb[0])
        created_bombs[created_bomb[0]]+=1
    else:
        casing-=5
        if casing>0:
            bomb_casings.append(casing)
        bomb_effects.appendleft(bomb)

if len(unique_bombs)==3:
    print(f'Bene! You have successfully filled the bomb pouch!')
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects)==1 and bomb_effects[0]<0:
    bomb_effects.pop()

if len(bomb_casings)==1 and bomb_casings[0]<0:
    bomb_casings.pop()


if len(bomb_effects)!=0:
    if bomb_effects.pop()!=0:
        print(f'Bomb Effects: {", ".join(map(str,bomb_effects))}')
else:
    print(f'Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join(map(str,bomb_casings))}')
else:
    print(f'Bomb Casings: empty')

print(f"Cherry Bombs: {created_bombs['CHERRY']}")
print(f"Datura Bombs: {created_bombs['DATURA']}")
print(f"Smoke Decoy Bombs: {created_bombs['SMOKE_DECOY']}")
