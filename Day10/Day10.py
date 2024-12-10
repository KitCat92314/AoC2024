lines = []
file = open("Day10.txt", "r")
for i in file:
    lines.append(i.strip())

def finder(nums):
    sum = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == '0':
                found = []
                sum += find(i, j, 0, nums, found)
    print(sum)

def find(x, y, target, nums, found):
    sum = 0
    if int(nums[x][y]) == target:
        if target == 9:
            return 1
        if x + 1 < len(nums):
            sum += find(x + 1, y, target + 1, nums, found)
        if x - 1 > -1:
            sum += find(x - 1, y, target + 1, nums, found)
        if y + 1 < len(nums[0]):
            sum += find(x, y + 1, target + 1, nums, found)
        if y - 1 > -1:
            sum += find(x, y - 1, target + 1, nums, found)
    return sum

finder(lines)