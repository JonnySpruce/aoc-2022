from functools import reduce

BAGS_TO_CHECK = 3

def value(char):
    ascii_value = ord(char)
    if ascii_value >= 97:
        return ascii_value - 96
    return ascii_value - (64 - 26)

lines = open('./day3/input/input.txt','r').read().splitlines()
sum = 0

for line_index in range(0, len(lines), BAGS_TO_CHECK):
    bags = lines[line_index:line_index + BAGS_TO_CHECK]
    char = reduce(lambda x, y: set(x).intersection(set(y)), bags).pop()
    sum += value(char)
    print(char, value(char))

print(sum)
