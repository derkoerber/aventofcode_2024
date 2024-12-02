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

distances: List[int] = []

for idx, pointer1 in enumerate(list1):
    pointer2 = list2[idx]
    if pointer1 > pointer2:
        distances.append(pointer1 - pointer2)
    else:
        distances.append(pointer2 - pointer1)

sum: int = 0

for distance in distances:
    sum += distance

print(sum)
