with open('./text.txt') as f:
    result = list(f)[0::2]
    for line in result:
        line = line.replace('\n', "")
        for ch in ["-", ",", ".", "!", "?"]:
            if ch in line:
                line = line.replace(ch, "@")
        words=list(reversed(line.split(' ')))
        print(f'{" ".join(words)}')
