n=int(input())
elements=set()

for num in range(n):
    molecules=tuple(input().split(' '))
    for molecule in molecules:
        elements.add(molecule)

for e in elements:
    print(e)