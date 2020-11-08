import os
from collections import defaultdict

directory = input()

list_ = os.listdir(directory)
dict = defaultdict(list)

for item in list_:
    item = item.split('.')
    dict[item[-1]].append('.'.join(item[:-1]))
    # print(item)

sorted_dict = sorted(dict.items(), key = lambda x: x[0])

for key, files in sorted_dict:
    print(f'.{key}')
    for file in sorted(files):
        print(f'---{file}')
