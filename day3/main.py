import os
from typing import List


def parse_input(file_path: str = "input.txt") -> List[int]:
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, file_path)
    memory:str = ""
    
    with open(full_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            memory += line.strip()

    return memory

def calculate_mul(mul_appendix: str) -> int:
    s_index = mul_appendix.find("(")
    if s_index == 0:
        e_index = mul_appendix.find(")")
        if e_index > 0:
            mul_content = mul_appendix[s_index + 1:e_index]
            mul_numbers = mul_content.split(',')

            if len(mul_numbers) == 2 and len(mul_numbers[0]) <= 3 and len(mul_numbers[1]) <= 3:
                if mul_numbers[0].isdigit() and mul_numbers[1].isdigit():
                    return int(mul_numbers[0]) * int(mul_numbers[1])
    return 0

def part_1(memory: str):
    result = 0

    mul_list = memory.split('mul')
    for mul_appendix in mul_list:
        multiplied = calculate_mul(mul_appendix)
        result += multiplied

    return result

def part_2(memory: str):
    result = 0
    do = True
    
    mul_list = memory.split('mul')
    for idx, mul_appendix in enumerate(mul_list):
        if idx > 0:
            if mul_list[idx -1].find("do()") > -1:
                do = True
            elif mul_list[idx -1].find("don't()") > -1:
                do = False

        if do == True:
            multiplied = calculate_mul(mul_appendix)
            result += multiplied

    return result

def process(memory: str, type: str = "p1") -> int:
    if type == "p1":
        return part_1(memory)
    else:
        return part_2(memory)

def run():
    corrupted_memory = parse_input()
    result_1 = process(corrupted_memory, "p1")
    print(f"The result for the computer (part1) is {result_1}")
    result_2 = process(corrupted_memory, "p2")
    print(f"The result for the computer (part2) is {result_2}")

if __name__ == '__main__':
    run()

