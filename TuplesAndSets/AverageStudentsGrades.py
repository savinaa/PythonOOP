import collections

num=int(input())
dict=collections.defaultdict(list)
a=sorted(dict)
for _ in range(num) :
    name,grade=tuple(input().split(' '))
    dict[name].append(float(grade))
for name, grades in dict.items():
    grades_list=' '.join(map(lambda f:format(f,'.2f'),grades))
    print(f'{name } -> {grades_list} (avg: {format(sum(grades)/len(grades),".2f")})')