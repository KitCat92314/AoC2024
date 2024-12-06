file = open("Day6.txt", "r")
lines = []
barricade = (-1, -1)
locations = []
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
            elif self.location[0] - 1 == barricade[0] and self.location[1] == barricade[1]:
                self.turn()
            else:
                self.location[0] -= 1
        elif self.dir == 1:
            if self.location[1] + 1 > len(map[self.location[0]]) - 1:
                return True
            elif map[self.location[0]][self.location[1] + 1] == '#':
                self.turn()
            elif self.location[0] == barricade[0] and self.location[1] + 1 == barricade[1]:
                self.turn()
            else:
                self.location[1] += 1
        elif self.dir == 2:
            if self.location[0] + 1 > len(map) - 1:
                return True
            elif map[self.location[0] + 1][self.location[1]] == '#':
                self.turn()
            elif self.location[0] + 1 == barricade[0] and self.location[1] == barricade[1]:
                self.turn()
            else:
                self.location[0] += 1
        elif self.dir == 3:
            if self.location[1] - 1 < 0:
                return True
            elif map[self.location[0]][self.location[1] - 1] == '#':
                self.turn()
            elif self.location[0] == barricade[0] and self.location[1] - 1 == barricade[1]:
                self.turn()
            else:
                self.location[1] -= 1
        if self.memoize(visited) > 1000:
            locations.append(barricade)
            return True

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
            dictionary[self.location[0]] = [set(), 0]
        dictionary[self.location[0]][0].add(self.location[1])
        dictionary[self.location[0]][1] += 1
        return dictionary[self.location[0]][1]
        
def count():
    sum = 0
    for i in visited:
        sum += len(visited[i][0])
    print(sum)

def locs():
    global barricade
    g = guard(lines)
    g.run(lines)
    places = visited.copy()
    for i in places:
        for j in places[i][0]:
            barricade = (i, j)
            visited.clear()
            test = guard(lines)
            test.run(lines)
    print(len(locations))

locs()
# g = guard(lines)
# g.run(lines)
# count()