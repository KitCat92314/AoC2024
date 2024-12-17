import re
file = open("Day14.txt", "r")
input = []
for i in file:
    nums = re.findall("-*[0-9]+", i)
    p = (int(nums[0]), int(nums[1]))
    v = (int(nums[2]), int(nums[3]))
    input.append((p, v))

def positions(blinks, x, y):
    p_final = dict()
    for pair in input:
        px, py = pair[0]
        vx, vy = pair[1]
        pf = ((vx * blinks + px) % x, (vy * blinks + py) % y)
        if pf in p_final:
            p_final[pf] += 1
        else:
            p_final[pf] = 1
    
    q1, q2, q3, q4 = 0, 0, 0, 0
    for pos in p_final:
        if pos[0] < x // 2 and pos[1] < y // 2:
            q1 += p_final[pos]
        elif pos[0] > x // 2 and pos[1] < y // 2:
            q2 += p_final[pos]
        elif pos[0] < x // 2 and pos[1] > y // 2:
            q3 += p_final[pos]
        elif pos[0] > x // 2 and pos[1] > y // 2:
            q4 += p_final[pos]
    # print(q1 * q2 * q3 * q4)
    return p_final

# positions(100, 101, 103)
# time = 0
# while True:
#     picture = [[0 for _ in range(103)] for _ in range(101)]
#     places = positions(time, 101, 103)
#     xs = dict()
#     ys = dict()
#     for x, y in places:
#         picture[x][y] = 1
#         if x not in xs:
#             xs[x] = []
#             xs[x].append(y)
#         else:
#             xs[x].append(y)
#         if y not in ys:
#             ys[y] = []
#             ys[y].append(x)
#         else:
#             ys[y].append(x)
#     for x in xs:
#         for y in ys:
#             if len(xs[x]) > 20 and len(ys[y]) > 20:
#                 print(time)
#     time += 1

def print_picture(time):
    picture = [[0 for _ in range(103)] for _ in range(101)]
    places = positions(time, 101, 103)
    for x, y in places:
        picture[x][y] = 1
    output = open("Day14p.txt", 'w')
    for line in picture:
        for point in line:
            print(point, end="", file=output)
        print("", file=output)

print_picture(7502)