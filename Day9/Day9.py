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
    
    # d = 0
    # f = 0
    cont = True
    files.reverse()
    i = 0
    while cont:
        while i < len(files):
            if dots[0][1] >= files[i][1]:
                for it in range(files[i][1]):
                    space[files[i][0] + it], space[dots[0][0] + it] = space[dots[0][0] + it], space[files[i][0] + it]
                files.pop(i)
                print(space)
                dots = recount(space)
                i = 0
                break
            i += 1
        
def recount(line):
    dots = []
    counter = 0
    for idx in range(len(line)):
        if line[idx] == '.':
            counter += 1
        elif counter != 0:
            dots.append((idx - 1, counter))
            counter = 0
    print(dots)
    return dots
    
    

bar(lines[0])