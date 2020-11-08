import collections
def numbers_searching(*args):
    min_value=min(args)
    max_value=max(args)
    min_value_index=args.index(min_value)
    max_value_index=args.index(max_value)

    sub_args=args[min(min_value_index,max_value_index):max(min_value_index,max_value_index)+1]
    seq=[x for x in range(min_value,max_value+1)]
    set_subargs=set(sub_args)
    set_seq=set(seq)
    missing=set_seq-set_subargs

    result=[]
    result.append(int(missing.pop()))

    dict=collections.defaultdict(int)
    sub_result=[]
    for value in args:
        dict[value]+=1
    for key in dict:
        if dict[key]>1:
            sub_result.append(key)
    result.append(sub_result)
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
