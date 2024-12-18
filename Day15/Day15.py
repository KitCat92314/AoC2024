import copy
matrix = []
moves = []
input = []
sub = []
file = open("Day15.txt", "r")
for i in file:
    input.append(i.strip())

def read_in():
    global sub
    mapping = True
    for i in range(len(input)):
        if len(input[i]) < 3:
            mapping = False
        if mapping:
            line = []
            for j in range(len(input[i])):
                if input[i][j] == '@':
                    sub = [len(matrix), len(line)]
                    line.append('.')
                    line.append('.')
                    continue
                if input[i][j] == 'O':
                    line.append('[')
                    line.append(']')
                    continue
                line.append(input[i][j])
                line.append(input[i][j])
            matrix.append(line)
        else:
            for j in range(len(input[i])):
                moves.append(input[i][j])
    # map = copy.deepcopy(matrix)
    # map[sub[0]][sub[1]] = "@"
    # output = open("Day15p.txt", "w")
    # for i in map:
    #     for j in i:
    #         print(j, end="", file=output)
    #     print("", file=output)
    # output.close()

def move():
    global matrix
    while moves:
        backup = copy.deepcopy(matrix)
        if moves[0] == '^':
            if matrix[sub[0] - 1][sub[1]] == '[' or matrix[sub[0] - 1][sub[1]] == ']':
                if not move_box((sub[0] - 1, sub[1]), (-1, 0)):
                    matrix = copy.deepcopy(backup)
            if matrix[sub[0] - 1][sub[1]] == '.':
                sub[0] -= 1
        elif moves[0] == 'v':
            if matrix[sub[0] + 1][sub[1]] == '[' or matrix[sub[0] + 1][sub[1]] == ']':
                if not move_box((sub[0] + 1, sub[1]), (1, 0)):
                    matrix = copy.deepcopy(backup)
            if matrix[sub[0] + 1][sub[1]] == '.':
                sub[0] += 1
        elif moves[0] == '<':
            if matrix[sub[0]][sub[1] - 1] == '[' or matrix[sub[0]][sub[1] - 1] == ']':
                if not move_box((sub[0], sub[1] - 1), (0, -1)):
                    matrix = copy.deepcopy(backup)
            if matrix[sub[0]][sub[1] - 1] == '.':
                sub[1] -= 1
        elif moves[0] == '>':
            if matrix[sub[0]][sub[1] + 1] == '[' or matrix[sub[0]][sub[1] + 1] == ']':
                if not move_box((sub[0], sub[1] + 1), (0, 1)):
                    matrix = copy.deepcopy(backup)
            if matrix[sub[0]][sub[1] + 1] == '.':
                sub[1] += 1
        moves.pop(0)
        print(sub)
    # map = copy.deepcopy(matrix)
    # map[sub[0]][sub[1]] = "@"
    # output = open("Day15p.txt", "w")
    # for i in map:
    #     for j in i:
    #         print(j, end="", file=output)
    #     print("", file=output)
    # output.close()

def move_box(pos, dir):
    moving = set()
    return _move_box(pos, dir, moving)

def _move_box(pos, dir, moving):
    x, y = pos
    moved = []
    moving.add((x, y))
    if matrix[x + dir[0]][y + dir[1]] == '[' or matrix[x + dir[0]][y + dir[1]] == ']':
        if (x + dir[0], y + dir[1]) not in moving:
            moved.append(_move_box((x + dir[0], y + dir[1]), dir, moving))
    if dir != (0, 1) and matrix[x][y] == "[":
        if (x, y + 1) not in moving:
            moved.append(_move_box((x, y + 1), dir, moving))
    if dir != (0, -1) and matrix[x][y] == "]":
        if (x, y - 1) not in moving:
            moved.append(_move_box((x, y - 1), dir, moving))
    if matrix[x + dir[0]][y + dir[1]] == ".":
        matrix[x + dir[0]][y + dir[1]], matrix[x][y] = matrix[x][y], matrix[x + dir[0]][y + dir[1]]
        return all(moved)
    return False
    
def count():
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "[":
                sum += 100 * i + j
    print(sum)


read_in()
move()
count()