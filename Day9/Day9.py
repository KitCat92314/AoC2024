import math
import re

lines = []
file = open("Day9.txt", "r")
for i in file:
    lines.append(i)

def foo(line):
    space = []
    doc = 0
    for i in range(len(line)):
        if i % 2 == 0:
            for _ in range(int(line[i])):
                space.append(doc)
            doc += 1
        else:
            for _ in range(int(line[i])):
                space.append('.')
    x = len(space) - 1
    y = 0
    while x > y:
        while x > 0 and space[x] == '.':
            x -= 1
        while y < len(space) - 1 and space[y] != '.':
            y += 1
        if y < x:
            space[x], space[y] = space[y], space[x]
    sum = 0
    for idx in range(len(space)):
        if space[idx] != '.':
            sum += idx * int(space[idx])
    print(sum)

def bar(line):
    space = []
    doc = 0
    k = 0
    dots = []
    files = []
    for i in range(len(line)):
        if i % 2 == 0:
            for _ in range(int(line[i])):
                space.append(doc)
            files.append((k, int(line[i])))
            doc += 1
            k += int(line[i])
        else:
            for _ in range(int(line[i])):
                space.append('.')
            dots.append((k, int(line[i])))
            k += int(line[i])
    
    files.reverse()
    swapping = True
    while swapping:
        swapping = False
        x = 0
        while x < len(files):
            y = 0
            while y < len(dots):
                if dots[y][1] >= files[x][1] and dots[y][0] < files[x][0]:
                    for idx in range(files[x][1]):
                        space[dots[y][0] + idx], space[files[x][0] + idx] = space[files[x][0] + idx], space[dots[y][0] + idx]
                    dots = recount(space)
                    files.pop(x)
                    swapping = True
                else:
                    y += 1
            x += 1
    sum = 0
    for idx in range(len(space)):
        if space[idx] != '.':
            sum += idx * int(space[idx])
    print(sum)

        
def recount(line):
    dots = []
    counter = 0
    for idx in range(len(line)):
        if line[idx] == '.':
            counter += 1
        elif counter != 0:
            dots.append((idx - counter, counter))
            counter = 0
    print(dots)
    return dots
    
    

bar(lines[0])