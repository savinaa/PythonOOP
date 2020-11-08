import collections

dict=collections.defaultdict(int)
num=0
while True:
    token=input()
    if token.isdigit():
        num=int(token)
        break
    name,telephone=token.split('-')
    dict[name]=telephone

for i in range(num):
    person=input()
    if person in dict:
        telephone=dict[person]
        print(f'{person} -> {telephone}')
    else:
        print(f'Contact {person} does not exist.')
