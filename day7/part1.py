import re
from pathlib import Path

MAX_SEARCH_SIZE = 100000

class File():
    name: str
    path: Path
    size: int

    def __init__(self, name: str, parent_path: Path, size: int) -> None:
        super().__init__()
        self.name = name
        self.path = parent_path.joinpath(name)
        self.size = size


class Directory():
    name: str
    path: Path
    files: list[File]
    dirs: list['Directory']
    _size: int

    def __init__(self, path: Path, files: list[File]) -> None:
        super().__init__()
        self.name = path.parts[-1]
        self.path = path
        self.files = files
        self.dirs = []
        self._size = None

    @property
    def size(self) -> int:
        if not self._size:
            self._size = self.calc_size()
        return self._size

    def calc_size(self) -> int:
        return sum([item.size for item in self.files + self.dirs])

    def add_child_dir(self, dir) -> None:
        self.dirs.append(dir)



def parse_commands(commands: list[str]) -> dict[Directory]:
    directories: dict[Directory] = {}
    current_path = Path('/')

    for idx, command in enumerate(commands):
        if command.startswith('$ cd ..'):
            current_path = current_path.parent
        elif match := re.search(r'\$ cd (.*)', command):
            dir = match.group(1)
            current_path = current_path.joinpath(dir)
        elif command.startswith('$ ls'):
            ls_output = find_ls_output(commands[idx + 1:])
            current_dir = parse_ls(current_path, ls_output)
            directories[current_path] = current_dir
            if current_path != current_path.parent:
                directories[current_path.parent].add_child_dir(current_dir)

    return directories



def find_ls_output(other_commands: list[str]) -> list[str]:
    ls_output = []
    for output in other_commands:
        if not output.startswith('$'):
            ls_output.append(output)
        else:
            break
    return ls_output


def parse_ls(current_path: Path, ls_output: list[str]) -> Directory:
    files = [File(match.group(2), current_path, int(match.group(1))) for line in ls_output if (match := re.search("(\d+) (\S+)", line))]
    return Directory(current_path, files)


lines = open('./day7/input/input.txt','r').read().splitlines()
dirs = parse_commands(lines)

sum_match_dirs = sum([size for dir in dirs.values() if (size := dir.size) <= MAX_SEARCH_SIZE])

print(sum_match_dirs)