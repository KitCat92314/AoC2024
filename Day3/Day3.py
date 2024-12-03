import re
def find_mul(data):
    sum = 0
    do = True
    found = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data)
    for i in found:
        if i == "do()":
            do = True
            continue
        elif i == "don't()":
            do = False
            continue
        nums = re.findall("[0-9]+", i)
        if do:
            sum += int(nums[0]) * int(nums[1])
    return sum

with open("Day3.txt", "r") as file:
    data = file.read().replace("\n", "")
print(find_mul(data))


        