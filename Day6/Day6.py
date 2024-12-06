file = open("Day6.txt", "r")
lines = []
visited = dict()
for i in file:
    lines.append(i)

class guard():
    def __init__(self, map):
        self.location = [0, 0]
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '^':
                    self.location = [i, j]
        self.memoize(visited)
        self.dir = 0
    
    def move(self, map):
        if self.dir == 0:
            if self.location[0] - 1 < 0:
                return True
            elif map[self.location[0] - 1][self.location[1]] == '#':
                self.turn()
            else:
                self.location[0] -= 1
        elif self.dir == 1:
            if self.location[1] + 1 > len(map[self.location[0]]) - 1:
                return True
            elif map[self.location[0]][self.location[1] + 1] == '#':
                self.turn()
            else:
                self.location[1] += 1
        elif self.dir == 2:
            if self.location[0] + 1 > len(map) - 1:
                return True
            elif map[self.location[0] + 1][self.location[1]] == '#':
                self.turn()
            else:
                self.location[0] += 1
        elif self.dir == 3:
            if self.location[1] - 1 < 0:
                return True
            elif map[self.location[0]][self.location[1] - 1] == '#':
                self.turn()
            else:
                self.location[1] -= 1
        self.memoize(visited)
    
    def turn(self):
        self.dir += 1
        if self.dir > 3:
            self.dir = 0

    def run(self, map):
        moving = False
        while not moving:
            moving = self.move(map)
    
    def memoize(self, dictionary):
        if self.location[0] not in dictionary:
            dictionary[self.location[0]] = set()
        dictionary[self.location[0]].add(self.location[1])
        
def count():
    sum = 0
    for i in visited:
        sum += len(visited[i])
    print(sum)

g = guard(lines)
g.run(lines)
count()