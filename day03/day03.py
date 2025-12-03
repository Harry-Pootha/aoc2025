from utils import FileMode
from utils import read_file
from utils import digits_in_string, list_to_string
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

def find_smallest_position(numbers: list[int]) -> int:
    smallest: int = 9
    smallest_pos: int = 0

    for position, number in enumerate(numbers):
        if number < smallest:
            smallest = number
            smallest_pos = position

    return smallest_pos

def find_last_smallest_position(numbers: list[int]) -> int:
    smallest: int = 9
    smallest_pos: int = 0

    for position, number in enumerate(numbers):
        if number <= smallest:
            smallest = number
            smallest_pos = position

    return smallest_pos

def remove_first_smallest(numbers: list[int]) -> list[int]:
    numbers_transformed = numbers.copy()
    numbers_transformed.pop(find_smallest_position(numbers_transformed))
    return numbers_transformed

def remove_last_smallest(numbers: list[int]) -> list[int]:
    numbers_transformed = numbers.copy()
    numbers_transformed.pop(find_last_smallest_position(numbers_transformed))
    return numbers_transformed

def is_rising(left: int, right: int) -> bool:
    return right > left or right == left

def get_rising_change_position(numbers: list[int]) -> int:
    start_direction = is_rising(numbers[0], numbers[1])

    for position in range(0, len(numbers) - 2):
        if start_direction != is_rising(numbers[position], numbers[position + 1]):
            return position + 2 # why +2? I don't know why just found out with debugging

    return len(numbers) - 1

# always remove the leftmost smallest
def get_joltage_ext(numbers: list[int], limit: int) -> int:
    joltage: int

    while len(numbers) > limit:
        rising_change_pos = get_rising_change_position(numbers)
        position_to_remove = find_last_smallest_position(numbers[:rising_change_pos])
        numbers.pop(position_to_remove)

    joltage = int(list_to_string(numbers))
    return joltage

def remove_lowest_number(numbers: list[int], limit: int) -> list[int]:
    return_list: list[int] = numbers.copy()
    length = len(return_list)

    for smallest in range(0, 10):
        for position in range(length - 1, -1, -1): # what a stupid looking range
            number = return_list[position]
            if number == smallest:
                return_list.pop(position)
                length -= 1
                if length <= limit:
                    return return_list

    return return_list

def solve_ch1(mode: FileMode):
    file_content = read_file(FILES[mode])
    total_joltage: int = 0
    for line in file_content:
        line = line.strip()
        if line != "":
            total_joltage += int(get_joltage(line))

    print(F"Total Joltage: {total_joltage}")

def solve_ch2(mode: FileMode):
    file_content = read_file(FILES[mode])
    total_joltage: int = 0
    for line in file_content:
        line = line.strip()
        if line != "":
            joltage = get_joltage_ext(digits_in_string(line), 10)
            print(F"Current Joltage: {joltage}")
            total_joltage += int(joltage)
    print(F"Total Joltage: {total_joltage}")