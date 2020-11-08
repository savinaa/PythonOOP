def even_odd(*args):
    command=args[len(args)-1]
    args=args[0:len(args)-1]
    if command=='even':
        return list(filter(lambda x:x%2==0,args))
    else:
        return list(filter(lambda x: x % 2 != 0, args))

