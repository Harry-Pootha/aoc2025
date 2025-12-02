from math import remainder

from utils import FileMode
from utils import read_file
from typing import Final

FILES: dict[int, str] = dict()
FILES[FileMode.REAL] = "day01/input.txt"
FILES[FileMode.EXAMPLE] = "day01/example.txt"

MIN_ROTATION_VALUE: Final[int] = 0
MAX_ROTATION_VALUE: Final[int] = 100
START_ROTATION_VALUE: Final[int] = 50


def sub_clamp(left: int, right: int, lower_end: int = MIN_ROTATION_VALUE, upper_end: int = MAX_ROTATION_VALUE):
    clamp_difference = upper_end - lower_end
    sub_diff = (left - right) % clamp_difference

    if sub_diff >= MIN_ROTATION_VALUE:
        return sub_diff

    return MAX_ROTATION_VALUE - sub_diff

def add_clamp(left: int, right: int, lower_end: int = MIN_ROTATION_VALUE, upper_end: int = MAX_ROTATION_VALUE):
    clamp_difference = upper_end - lower_end
    return (left + right) % clamp_difference


def solve_ch1(mode: FileMode):
    rotation_sequence = read_file(FILES[mode])
    current_rotation_value = START_ROTATION_VALUE
    total_zero_rotations = 0

    print(F"Current rotation value: {current_rotation_value}")

    for rotation in rotation_sequence:
        direction = rotation[0]
        rotation_distance = int(rotation[1::])

        if direction == "L":
            current_rotation_value = sub_clamp(current_rotation_value, rotation_distance)
        else:
            current_rotation_value = add_clamp(current_rotation_value, rotation_distance)

        print(F"Current rotation value: {current_rotation_value}")

        if current_rotation_value == 0:
            total_zero_rotations += 1

    print(F"Password: {total_zero_rotations}")

def solve_ch2(mode: FileMode):
    rotation_sequence = read_file(FILES[mode])
    current_rotation_value = START_ROTATION_VALUE
    total_zero_hits = 0

    for rotation in rotation_sequence:
        direction = rotation[0]
        rotation_distance = int(rotation[1::])
        min_max_diff = MAX_ROTATION_VALUE - MIN_ROTATION_VALUE

        total_zero_hits += int(rotation_distance / min_max_diff)
        remaining_difference = rotation_distance % min_max_diff

        if direction == "L":
            if current_rotation_value != 0:
                if current_rotation_value - remaining_difference < MIN_ROTATION_VALUE:
                    total_zero_hits += 1
            current_rotation_value = sub_clamp(current_rotation_value, remaining_difference)
        else:
            if current_rotation_value != 0:
                if current_rotation_value + remaining_difference > MAX_ROTATION_VALUE:
                    total_zero_hits += 1
            current_rotation_value = add_clamp(current_rotation_value, remaining_difference)

        if current_rotation_value == 0:
            total_zero_hits += 1

    print(F"Password: {total_zero_hits}")
