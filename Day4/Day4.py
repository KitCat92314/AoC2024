import re
file = open("Day4.txt", "r")
rows = []
for i in file:
    rows.append(i)

def find(lines):
    sum = 0
    for i in lines:
        found = re.findall("XMAS", i)
        sum += len(found)
        found = re.findall("SAMX", i)
        sum += len(found)
    for line in range(len(lines) - 3):
        for char in range(len(lines[line])):
            if lines[line][char] == 'X':
                if lines[line + 1][char + 1] == 'M':
                    if lines[line + 2][char + 2] == 'A':
                        if lines[line + 3][char + 3] == 'S':
                            sum += 1
            if lines[line][char] == 'S':
                if lines[line + 1][char + 1] == 'A':
                    if lines[line + 2][char + 2] == 'M':
                        if lines[line + 3][char + 3] == 'X':
                            sum += 1
            if lines[line][char] == 'X':
                if lines[line + 1][char] == 'M':
                    if lines[line + 2][char] == 'A':
                        if lines[line + 3][char] == 'S':
                            sum += 1
            if lines[line][char] == 'S':
                if lines[line + 1][char] == 'A':
                    if lines[line + 2][char] == 'M':
                        if lines[line + 3][char] == 'X':
                            sum += 1
    for line in range(len(lines) - 3):
        for char in range(3, len(lines[line])):
            if lines[line][char] == 'S':
                if lines[line + 1][char - 1] == 'A':
                    if lines[line + 2][char - 2] == 'M':
                        if lines[line + 3][char - 3] == 'X':
                            sum += 1
            if lines[line][char] == 'X':
                if lines[line + 1][char - 1] == 'M':
                    if lines[line + 2][char - 2] == 'A':
                        if lines[line + 3][char - 3] == 'S':
                            sum += 1
    return sum

def find_mas(lines):
    sum = 0
    for line in range(len(lines) - 2):
        for char in range(len(lines[line]) - 2):
            if lines[line][char] == 'M':
                if lines[line + 2][char] == 'M':
                    if lines[line + 1][char + 1] == 'A' and lines[line][char + 2] == 'S' and lines[line + 2][char + 2] == 'S':
                        sum += 1
                elif lines[line][char + 2] == 'M':
                    if lines[line + 1][char + 1] == 'A' and lines[line + 2][char] == 'S' and lines[line + 2][char + 2] == 'S':
                        sum += 1
            if lines[line][char] == 'S':
                if lines[line + 2][char] == 'S':
                    if lines[line + 1][char + 1] == 'A' and lines[line][char + 2] == 'M' and lines[line + 2][char + 2] == 'M':
                        sum += 1
                elif lines[line][char + 2] == 'S':
                    if lines[line + 1][char + 1] == 'A' and lines[line + 2][char] == 'M' and lines[line + 2][char + 2] == 'M':
                        sum += 1
    return sum

print(find_mas(rows))