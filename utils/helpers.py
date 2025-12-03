
def read_file(path: str) -> list[str]:
    entries: list[str] = list()

    with open(path, "r") as file:
        for line in file:
            if not line == "":
                entries.append(line)

    return entries

def chars_in_string(string: str) -> list[str]:
    chars: list[str] = list()
    for char in string:
        chars.append(char)

    return chars

def ints_from_strings(strings: list[str]) -> list[int]:
    ints: list[int] = list()
    for string in strings:
        ints.append(int(string))
    return ints

def digits_in_string(string: str) -> list[int]:
    return ints_from_strings(chars_in_string(string))

def list_to_string(values: list) -> str:
    string: str = ""
    for value in values:
        string += F"{value}"
    return string