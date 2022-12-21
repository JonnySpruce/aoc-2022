import re

lines = open('./day5/input/input.txt','r').read().splitlines()

def extract_boxes(lines: list[str]) -> list[list[str]]:
    box_info_vals = [[char for char in line[1::4]] for line in lines]
    box_info_vals_rows = list(zip(*box_info_vals[::-1]))
    return [[char for char in row if char != ' '] for row in box_info_vals_rows]

def extract_instructions(lines: list[str]) -> list[list[int]]:
    matches = [re.search('\w+ (\d+) \w+ (\d+) \w+ (\d+)', line) for line in lines]
    instruction_lines = [[match_line.group(1), match_line.group(2), match_line.group(3),] for match_line in matches]
    single_instructions = []
    [single_instructions.extend([[int(line[1]) - 1, int(line[2]) - 1]] * int(line[0])) for line in instruction_lines]
    return single_instructions

def execute_instructions(boxes: list[list[str]], instructions: list[list[int]]) -> list[list[str]]:
    for instruction in instructions:
        box = boxes[instruction[0]].pop()
        boxes[instruction[1]].append(box)
    return boxes

def top_boxes(boxes: list[list[str]]) -> list[str]:
    return ''.join([row.pop() for row in boxes])


blank_line_idx = lines.index('')
boxes = extract_boxes(lines[:blank_line_idx-1])
instructions = extract_instructions(lines[blank_line_idx+1:])
boxes = execute_instructions(boxes, instructions)
print(top_boxes(boxes))