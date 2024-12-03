import os
from typing import List


def parse_input(file_path: str = "input.txt") -> List[int]:
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, file_path)
    parsed_list = []
    
    with open(full_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            numbers = list(map(int, line.strip().split()))
            parsed_list.append(numbers)

    return parsed_list

def check_row(num_row: List[int]):
    differs: List[int] = []
    
    for idx, number in enumerate(num_row):
        if idx == len(num_row) - 1:
            differs.append((number - num_row[idx - 1]))
        else:
            differs.append((num_row[idx + 1] - number))

    diff_errors: int = 0

    for diff in differs:
        if diff == 0:
            diff_errors += 1

        if diff < 0:
            diff = diff * -1

        if diff > 3:
            diff_errors += 1

    type_errors: int = 0
    positive_count = sum(1 for d in differs if d >= 0)
    negative_count = sum(1 for d in differs if d <= 0)

    if len(differs) != positive_count or len(differs) != negative_count:
        print()
        if positive_count > negative_count:
            type_errors = negative_count
        else:
            type_errors = positive_count

    if diff_errors + type_errors > 0:
        return False

    return True

def process(num_list: List[int] = []) -> int:
    safe_counter = 0
    for num_row in num_list:
        if check_row(num_row) == True:
            safe_counter += 1
    
    return safe_counter

def run():
    num_list = parse_input()
    safe = process(num_list)
    print(f"{safe} examples are safe")

if __name__ == '__main__':
    run()

