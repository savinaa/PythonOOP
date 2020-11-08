dimensions=list(input().split(' '))
[[print(" ".join("{}{}{}".format(chr(97+row),chr(97++row+col),chr(97+row))
                 for col in range(int(dimensions[1]))))
  for row in range(0,int(dimensions[0]))]]