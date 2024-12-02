from typing import List


list1: List[int] = []
list2: List[int] = []

with open("input.txt", 'r') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        line = line.replace("\n", "")
        lineList = line.split("   ")
        for idx, lineNum in enumerate(lineList):
            if idx == 0:
                list1.append(int(lineNum))
            else:
                list2.append(int(lineNum))

list1.sort()
list2.sort()

similarities: List[int] = []

for idx, pointer1 in enumerate(list1):
    count: int = 0
    found: bool = False

    for pointer2 in list2:
        if pointer1 == pointer2:
            count += 1
            found = True
        elif found == True:
            break
    similarities.append(pointer1 * count)

sum: int = 0

for similarity in similarities:
    sum += similarity

print(sum)
