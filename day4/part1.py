def is_any_overlap(line):
    range1, range2 = extract_ranges(line)
    return is_lh_overlap(range1, range2) or is_lh_overlap(range2, range1)

def is_lh_overlap(range1, range2):
    return range1[0] <= range2[0] and range1[1] >= range2[1]

def extract_ranges(line: str):
    data = [extract_range_values(range) for range in line.split(',')]
    print(data)
    return data

def extract_range_values(range_str: str):
    value_list = range_str.split('-')
    return [int(val) for val in value_list]



lines = open('./day4/input/input.txt','r').read().splitlines()

print(len([line for line in lines if is_any_overlap(line)]))