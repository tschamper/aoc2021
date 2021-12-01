
def part1(data: list) -> int:
    counter: int = 0
    last_value: int = None
    for current_value in data:
        if last_value != None and last_value < current_value:
            counter += 1
        last_value = current_value
    return counter

def part2(data: list) -> int:
    window_size: int = 3
    windows = [sum(data[i: i + window_size]) for i in range(len(data) - window_size + 1)]
    return part1(windows)

if __name__ == '__main__':
    filename: str = "./data.txt"
    with open(filename, 'r') as file:
        data = file.readlines()
    data = list(map(int, data))
    result = part2(data)
    print(result)
 