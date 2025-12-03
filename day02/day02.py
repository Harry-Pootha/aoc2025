from math import ceil

from utils import FileMode
from utils import read_file

FILES: dict[int, str] = dict()
FILES[FileMode.REAL] = "day02/input.txt"
FILES[FileMode.EXAMPLE] = "day02/example.txt"

class Range:
    minimum: int
    maximum: int

    def __init__(self, minimum: int, maximum: int):
        self.minimum = minimum
        self.maximum = maximum

def get_ranges(content: str) -> list[Range]:
    ranges: list[Range] = list()

    for entry in content.split(","):
        lower = entry.split("-")[0]
        upper = entry.split("-")[1]
        ranges.append(Range(int(lower), int(upper)))
    return ranges

def split_string_in_chunks(string: str, chunk_size: int) -> list[str]:
    chunks: list[str] = list()
    for i in range(0, len(string), chunk_size):
        chunks.append(string[slice(i, i+chunk_size)])
    return chunks

def is_string_repeated(string: str) -> bool:
    for i in range(1, (len(string) // 2) + 1):
        check_dict: dict[str, int] = dict()
        for chunk in split_string_in_chunks(string, i):
            if chunk not in check_dict:
                check_dict[chunk] = 0
            check_dict[chunk] += 1
            if check_dict[chunk] == ceil(len(string) / i):
                return True
    return False



def is_id_valid_ch1(id_value: int) -> bool:
    id_str = str(id_value)
    if len(id_str) % 2 == 1:
        return True

    if id_str[:len(id_str) // 2] != id_str[len(id_str) // 2:]:
        return True

    return False

def is_id_valid_ch2(id_value: int) -> bool:
    return not is_string_repeated(str(id_value))


def add_invalid_ids_ch1(range_value: Range) -> int:
    sum_invalid_ids = 0
    for i in range(range_value.minimum, range_value.maximum + 1):
        if not is_id_valid_ch1(i):
            sum_invalid_ids += i
    return sum_invalid_ids

def add_invalid_ids_ch2(range_value: Range) -> int:
    sum_invalid_ids = 0
    for i in range(range_value.minimum, range_value.maximum + 1):
        if not is_id_valid_ch2(i):
            sum_invalid_ids += i
    return sum_invalid_ids


def solve_ch1(mode: FileMode):
    file_content = read_file(FILES[mode])
    ranges = get_ranges(file_content[0])
    total_invalid_ids = 0

    for range_value in ranges:
        total_invalid_ids += add_invalid_ids_ch1(range_value)

    print(F"Invalid IDs: {total_invalid_ids}")

def solve_ch2(mode: FileMode):
    file_content = read_file(FILES[mode])
    ranges = get_ranges(file_content[0])
    total_invalid_ids = 0

    for range_value in ranges:
        total_invalid_ids += add_invalid_ids_ch2(range_value)

    print(F"Invalid IDs: {total_invalid_ids}")
