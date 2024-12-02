list1 = []
list2 = []

with open("input.txt", 'r') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        line = line.replace("\n", "")
        if idx % 2:
            list1.append(line)
        else:
            list2.append(line)
