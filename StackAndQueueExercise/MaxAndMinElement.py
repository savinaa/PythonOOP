rounds=int(input())
stack=[]


for r in range(rounds):
    command=input().split(' ')
    if command[0]=='1':
        stack.append(int(command[1]))
    elif command[0]=='2':
        try:
            stack.pop()
        except:
            continue
    elif command[0] == '3':
        try:
            print(max(stack))
        except:
            continue
    elif command[0] == '4':
        try:
            print(min(stack))
        except:
            continue

while len(stack)>0:
    print(f'{stack.pop()}',end='')
    if len(stack)!=0:
        print(', ',end='')