max_col = 0
max_row = 0

def is_edge(idx: int, max: int):
    return idx == 0 or idx == max - 1


def init_visibility(row_idx: int, col_idx: int):
    if is_edge(row_idx, max_row) or is_edge(col_idx, max_col):
        return 1
    else:
        return None


def plot_dict(d) -> str:
    output = ''

    for row in range(max_row):
        for char in range(max_col):
            output += str(d[row][char])
        output += '\n'
    return output


def is_tree_visible_in_row(row: list[int], tree_idx: int) -> bool:
    check_tree_height = row[tree_idx]
    visible_left = next((False for tree_height in row[:tree_idx] if tree_height >= check_tree_height), True)
    visible_right = next((False for tree_height in row[tree_idx + 1:] if tree_height >= check_tree_height), True)

    return visible_left or visible_right


def is_tree_visible(height_map: list[list[int]], row: int, col: int) -> bool:
    tree_row = height_map[row]
    tree_col = [height_map[i][col] for i in range(max_row)]
    return is_tree_visible_in_row(tree_row, col) or is_tree_visible_in_row(tree_col, row)


def get_visibility_for_trees(height_map: list[list[int]], visibility_map: list[list[str]]):
    for r, row in enumerate(height_map):
        for c, tree_height in enumerate(row):
            if not visibility_map[r][c]:
                visibility_map[r][c] = 1 if is_tree_visible(height_map, r, c) else 0




lines = open('./day8/input/input.txt','r').read().splitlines()

max_row = len(lines)
max_col = len(lines[0])

trees: list[list[int]] = [[*line] for line in lines]
visibility:list[list[str]] = [[init_visibility(r, c) for c in range(max_col)] for r in range(max_row)]


print(plot_dict(trees))

get_visibility_for_trees(trees, visibility)

print(plot_dict(visibility))
print(sum([sum(row) for row in visibility]))