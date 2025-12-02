
def read_file(path: str) -> list[str]:
    entries: list[str] = list()

    with open(path, "r") as file:
        for line in file:
            if not line == "":
                entries.append(line)

    return entries