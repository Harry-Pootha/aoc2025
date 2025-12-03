from utils import FileMode
from utils import read_file
from typing import Tuple
from typing import Final

MAX_DIGIT: Final[int] = 9

FILES: dict[int, str] = dict()
FILES[FileMode.REAL] = "day03/input.txt"
FILES[FileMode.EXAMPLE] = "day03/example.txt"

def get_highest_with_index(line: str) -> Tuple[int, int]:
    highest: int = 0
    highest_pos: int = 0
    for pos, char in enumerate(line):
        int_val = int(char)
        if int_val > highest:
            highest = int_val
            highest_pos = pos
        if highest == MAX_DIGIT:
            break
    return highest, highest_pos

def get_joltage(line: str) -> str:
    highest: int
    highest_pos: int
    second_highest: int = 0
    second_highest_pos: int = 0
    highest, highest_pos = get_highest_with_index(line)

    if highest_pos == len(line) - 1:
        second_highest = get_highest_with_index(line[:-1])[0]
        return F" {second_highest}{highest}"
    else:
        second_highest = get_highest_with_index(line[highest_pos + 1:])[0]
        return F" {highest}{second_highest}"

def solve_ch1(mode: FileMode):
    file_content = read_file(FILES[mode])
    total_joltage = 0
    for line in file_content:
        line = line.strip()
        if line != "":
            total_joltage += int(get_joltage(line))

    print(F"Total Joltage: {total_joltage}")

def solve_ch2(mode: FileMode):
    file_content = read_file(FILES[mode])
