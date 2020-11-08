numbers=list(map(int,input().split(' ')))
positive=list(filter(lambda x:x>0,numbers))
negative=list(filter(lambda x:x<0,numbers))
sum_positive=sum(positive)
sum_negative=sum(negative)
print(sum_negative)
print(sum_positive)
if sum_positive>abs(sum_negative):
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')