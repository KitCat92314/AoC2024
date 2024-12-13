import re
with open("Day13.txt", "r") as file:
    lines = file.readlines()
pairs = []
a = 0
b = 0
sum = 0
for i in range(len(lines)):
    nums = re.findall("[0-9]+", lines[i])
    if i % 4 == 0:
        a = (int(nums[0]), int(nums[1]))
    elif i % 4 == 1:
        b = (int(nums[0]), int(nums[1]))
    elif i % 4 == 2:
        sum = (int(nums[0]) + 10000000000000, int(nums[1]) + 10000000000000)
    elif i % 4 == 3:
        pairs.append((a, b, sum))
    

def solve_eq(C1, C3, C2, C4, sum1, sum2):
    coef = sum1 / sum2
    factor = (C4 * coef - C2) / (C1 - C3 * coef)
    B = sum1 / (C2 + C1 * factor)
    
    if abs(round(B) - B) < 0.001:
        print(B)
        return round(3 * factor * B + B)

sum = 0
for i in pairs:
    temp = solve_eq(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
    sum += temp if temp is not None else 0
print(sum)