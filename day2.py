
def part1(command_list: list[tuple[int, int]]) -> tuple[int, int]:
    horizontal: int = 0
    depth: int = 0
    for direction, value in data:
        match direction:
            case "forward":
                horizontal += value
            case "down":
                depth += value
            case "up":
                depth -= value
    return horizontal, depth

def part2(data: list[tuple[int, int]]) -> tuple[int, int]:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0
    for direction, value in data:
        match direction:
            case "forward":
                horizontal += value
                depth += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value
    return horizontal, depth

if __name__ == '__main__':
    filename: str = "./data.txt"
    with open(filename, 'r') as file:
        data = file.readlines()

    data = list(map(lambda x: x.split(' '), data))
    data = list(map(lambda x: (x[0], int(x[1])), data))

    horizontal, depth = part2(data)

    print(f"Horizontal: {horizontal}, depth: {depth}, mul: {horizontal*depth}")
