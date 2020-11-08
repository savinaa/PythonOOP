output = open("output.txt","w")
with open('./text.txt') as f:
    result = f.readlines()
    index=1
    for line in result:
        line=line.replace('\n','')
        letters=0
        punctuations=0
        for symbol in line:
            symbol=symbol.lower()
            if symbol==' ':
                continue
            if 97<=ord(symbol)<=122 :
                letters+=1
            else:
                punctuations+=1
        line=format(f'Line {index}: {line} ({letters})({punctuations})\n')
        output.write(line)
        index+=1
