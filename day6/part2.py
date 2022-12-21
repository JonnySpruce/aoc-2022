UNIQUE_LEN = 14

def is_same_chars(chars):
    for idx, current_char in enumerate(chars):
        for char in chars[idx + 1:]:
            if current_char == char:
                return False
    return True


def get_first_non_buffer_index(chars):
    for idx in range(len(chars)):
        if (is_same_chars(chars[idx:idx + UNIQUE_LEN])):
            return idx + UNIQUE_LEN

input = open('./day6/input/input.txt','r').read().splitlines()[0]
print(get_first_non_buffer_index(input))

