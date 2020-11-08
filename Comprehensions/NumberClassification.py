values=list(map(int,input().split(', ')))
[print('Positive: '+", ".join("{}".format(value) for value in values if value>=0))]
[print('Negative: '+", ".join("{}".format(value) for value in values if value < 0))]
[print('Even: '+", ".join("{}".format(value) for value in values if value%2==0))]
[print('Odd: '+", ".join("{}".format(value) for value in values if value%2!=0))]