from functools import reduce
from itertools import groupby

lines = open('./day1/input/input.txt','r').readlines()

print(sum(sorted([sum([int(string) for string in group]) for key, group in groupby(lines, lambda s: s != "\n") if key])[-3:]))