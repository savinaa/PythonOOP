
print([ num for num in range(int(input()),int(input())+1)if any( [num%divisible==0 for divisible in range(2,11)]) ])