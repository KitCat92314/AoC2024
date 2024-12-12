import re
d = dict()
matrix = []
with open("Day12.txt", "r") as file:
    lines = file.readlines()
for i in range(len(lines)):
    temp = lines[i].strip()
    line = []
    for j in range(len(temp)):
        line.append(temp[j])
        if temp[j] not in d:
            d[temp[j]] = set()
        d[temp[j]].add((i, j))
    matrix.append(temp)

counted = set()

def bfs():
    sum = 0
    for letter in d:
        nodes = d[letter]
        visited = set()
        for n in nodes:
            if n not in visited:
                outside = []
                visited.add(n)
                tree = set()
                p = 0
                to_visit = [n]
                while to_visit:
                    node = to_visit.pop()
                    if node not in tree:
                        tree.add(node)
                        e = neighbors(node[0], node[1], letter, outside)
                        for edge in e:
                            visited.add(edge)
                            to_visit.append(edge)
                        p = len(outside)
                        for r in range(len(outside)):
                            for t in range(r + 1, len(outside)):
                                if is_neighbor(outside[r][0], outside[t][0]) and is_neighbor(outside[r][1], outside[t][1]):
                                    p -= 1
                sum += p * len(tree)
    return sum


def neighbors(x, y, letter, outside):
    ret = []
    if x - 1 > -1 and matrix[x - 1][y] == letter:
        ret.append((x - 1, y))
    else:
        outside.append([(x, y), (x - 1, y)])
    if x + 1 < len(matrix) and matrix[x + 1][y] == letter:
        ret.append((x + 1, y))
    else:
        outside.append([(x, y), (x + 1, y)])
    if y - 1 > -1 and matrix[x][y - 1] == letter:
        ret.append((x, y - 1))
    else:
        outside.append([(x, y), (x, y - 1)])
    if y + 1 < len(matrix[x]) and matrix[x][y + 1] == letter:
        ret.append((x, y + 1))
    else:
        outside.append([(x, y), (x, y + 1)])
    return ret

def is_neighbor(pair1, pair2):
    if abs(pair1[0] - pair2[0]) < 2 and abs(pair1[1] - pair2[1]) == 0 or abs(pair1[0] - pair2[0]) == 0 and abs(pair1[1] - pair2[1]) < 2:
        return True
    return False

print(matrix)
print(d)
print(bfs())