def value(char):
    ascii_value = ord(char)
    if ascii_value >= 97:
        return ascii_value - 96
    return ascii_value - (64 - 26)

lines = open('./day3/input/input.txt','r').read().splitlines()

sum = 0

for line in lines:
    line_split = int(len(line)/2)
    char = set(line[:line_split]).intersection(line[line_split:]).pop()
    sum += value(char)
    print(char, value(char))

print(sum)
