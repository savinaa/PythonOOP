names=input().split(', ')
player={}
for name in names:
    player[name]={}
while True:
    token=input().split("-")
    if len(token)!=3:
        break
    player_name=token[0]
    new_weapon=token[1]
    weapon_value=int(token[2])
    player_inventory=player[player_name]
    if new_weapon not in player_inventory:
        player_inventory[new_weapon]=weapon_value

[print(f'{name} -> Items: {len(player[name])}, Cost: {sum(player[name].values())}') for name in names]