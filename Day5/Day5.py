import re

file = open("Day5.txt", "r")
pairs = dict()
rev_pairs = dict()
lines = []
pairing = True
for i in file:
    if i == "break\n":
        pairing = False
        continue
    if pairing:
        nums = re.findall("[0-9]+", i)
        nums[0], nums[1] = int(nums[0]), int(nums[1])
        if nums[1] not in pairs:
            pairs[nums[1]] = set()
            pairs[nums[1]].add(nums[0])
        else:
            pairs[nums[1]].add(nums[0])
        if nums[0] not in rev_pairs:
            rev_pairs[nums[0]] = set()
            rev_pairs[nums[0]].add(nums[1])
        else:
            rev_pairs[nums[0]].add(nums[1])
    else:
        temp = []
        pages = re.findall("[0-9]+", i)
        for j in pages:
            temp.append(int(j))
        lines.append(temp)

def check_pages(pairs, line):
        for i in range(len(line)):
            if line[i] in pairs:
                for j in range(len(line) - 1, i, -1):
                    if line[j] in pairs[line[i]]:
                        return False, j
        return True, -1

def sum(lines, pairs):
    correct = []
    sum = 0
    for line in lines:
        correct.append(check_pages(pairs, line))
    for i in range(len(lines)):
        if correct[i]:
            sum += lines[i][len(lines[i])//2]
    return sum

def fix(lines, pairs):
    correct = []
    sum = 0
    for line in lines:
        correct.append(check_pages(pairs, line))
    for i in range(len(lines)):
        if not correct[i][0]:
            while not correct[i][0]:
                idx = correct[i][1]
                first = correct[i][1]
                for j in range(correct[i][1] - 1, -1, -1):
                    if lines[i][j] in rev_pairs[lines[i][idx]]:
                        first = j
                print(first)
                item = lines[i][idx]
                lines[i].insert(first, item)
                print(lines[i])
                lines[i].pop(idx + 1)
                print(lines[i])
                correct[i] = check_pages(pairs, lines[i])
            sum += lines[i][len(lines[i])//2]
            print(sum)
    return sum

print(fix(lines, pairs))