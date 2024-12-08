import math

lines = []
file = open("Day8.txt", "r")
for i in file:
    lines.append(i)

class point():
    def __init__(self, x, y, f, nothing = False):
        self.x = x
        self.y = y
        self.f = f
        self.nothing = nothing
    
    def calc_dist(self, other):
        return self.x - other.x, self.y - other.y
    
    def calc_dir(self, other):
        ret = math.atan2((self.x - other.x), (self.y - other.y))
        if ret < 0:
            ret += math.pi
        return ret

class map():
    def __init__(self, map):
        self.m = []
        self.where = dict()
        for i in range(len(map)):
            temp = []
            for j in range(len(map[i])):
                if map[i][j] == '\n':
                    continue
                elif map[i][j] != '.':
                    place = point(i, j, map[i][j])
                    temp.append(place)
                    self.where.setdefault(map[i][j], set())
                    self.where[map[i][j]].add(place)
                else:
                    temp.append(point(i, j, None, True))
            self.m.append(temp)
        
    def count(self):
        places = set()
        for i in map.coords(len(self.m), len(self.m[0])):
            for type in self.where:
                for node in self.where[type]:
                    for node2 in self.where[type]:
                        if node == node2:
                            continue
                        if self.m[i[0]][i[1]].calc_dir(node) == self.m[i[0]][i[1]].calc_dir(node2):
                            places.add(i)
                            continue
        for items in self.where:
            for some in self.where[items]:
                places.add((some.x, some.y))
        return len(places)
    
    def coords(x, y):
        for i in range(x):
            for j in range(y):
                yield i, j

m = map(lines)
print(m.count())

