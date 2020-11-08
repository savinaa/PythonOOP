from os import listdir,environ
from os.path import isfile
from os.path import join as j
from collections import OrderedDict
folder=input()
onlyfiles = [f for f in listdir(folder) if isfile(j(folder, f))]
dict_of_extensions=OrderedDict()
for file in onlyfiles:
    filename,extension=file.split('.')
    if extension not in dict_of_extensions:
        dict_of_extensions[extension]=[]
    dict_of_extensions[extension].append(file)
desktop_file=j(environ["HOMEPATH"], "Desktop/report.txt")
with open(desktop_file,'a+') as f:
    for key,value in dict_of_extensions.items():
        f.write(f'.{key}\n')
        value=sorted(value)
        for file in value:
            f.write(f'- - -{file}\n')



