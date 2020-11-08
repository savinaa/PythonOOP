import os
def create(filename):
    f = open(filename, "w+")
    f.close()


def add(filename, content):
    with open(filename,'a+') as f:
        f.write(content+'\n')


def replace(filename, old_str, new_str):
    path='./'
    isExist = os.path.exists(path+filename)
    if not isExist:
        print('An error occured')
    else:
        result=''
        with open(filename, 'r+') as f:
            data=f.readlines()
            for line in data:
                line=line.replace(old_str,new_str)
                result+=line
        with open(filename, "w") as f1:
            f1.writelines(result)



def delete(filename):
    path = './'
    isExist = os.path.exists(path + filename)
    if not isExist:
        print('An error occured')
    else:
        os.remove(filename)


while True:
    entry=input()
    if entry=='End':
        break
    tokens=entry.split('-')
    if tokens[0]=='Create':
        create(tokens[1])
    elif tokens[0]=='Add':
        add(tokens[1],tokens[2])
    elif tokens[0]=='Replace':
        replace(tokens[1],tokens[2],tokens[3])
    elif tokens[0]=='Delete':
        delete(tokens[1])