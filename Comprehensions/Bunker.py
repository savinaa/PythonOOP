categories=input().split(', ')
rounds=int(input())
dict={}
total_quantity=0
total_quality=0
for category in categories:
    dict[category] = []
for round in range(rounds):
    token=input().split(' - ')
    category=token[0]
    food=token[1]
    quantity,quality=token[2].split(';')
    total_quantity+=int(quantity.split(':')[1])
    total_quality+=int(quality.split(':')[1])
    if food not in dict[category]:
        dict[category].append(food)
print(f'Count of items: {total_quantity}\nAverage quality: '+"{:.2f}".format(total_quality/len(categories)))
[print(f'{category} -> {", ".join(dict[category])}')for category in categories]