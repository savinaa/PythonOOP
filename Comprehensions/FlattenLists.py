import itertools
matrix = [[col for col in row.strip().split(" ") if col] for row in reversed(input().split('|'))]
print(" ".join(itertools.chain(*matrix)))
