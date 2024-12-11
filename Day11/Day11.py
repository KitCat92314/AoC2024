import re
file = open("Day11.txt", "r")
lines = []
for i in file:
    lines.append(i)
nums = re.findall("[0-9]+", lines[0])
l = []
for i in nums:
    if i != " ":
        l.append(int(i))
memo = dict()
memo2 = dict()
memo[0] = 1

def blink(line, memo):
    i = 0
    while i < len(line):
        if line[i] in memo.keys():
            if hasattr(memo[line[i]], "__getitem__"):
                a, b = memo[line[i]]
                line.insert(i, a)
                line[i + 1] = b
                i += 1
            else:
                line[i] = memo[line[i]]
            i += 1
            continue
        if count_digits(line[i]) % 2 == 0:
            a, b = split(line[i])
            a = int(a)
            b = int(b)
            memo[line[i]] = (int(a), int(b))
            line.insert(i, int(a))
            line[i + 1] = int(b)
            i += 1
        else:
            memo[line[i]] = int(line[i]) * 2024
            line[i] = int(line[i]) * 2024
        i += 1
    return line

def blink_recr(num, memo, depth):
    len = 0
    print(depth)
    if depth == 75:
        return 1
    if (num, depth) in memo2.keys():
        return memo2[(num, depth)]
    if num in memo.keys():
        if hasattr(memo[num], "__getitem__"):
            a, b = memo[num]
            len += blink_recr(a, memo, depth + 1)
            len += blink_recr(b, memo, depth + 1)
        else:
            len += blink_recr(memo[num], memo, depth + 1)
    else:
        if count_digits(num) % 2 == 0:
            a, b = split(num)
            a = int(a)
            b = int(b)
            len += blink_recr(a, memo, depth + 1)
            len += blink_recr(b, memo, depth + 1)
        else:
            a = num * 2024
            memo[num] = a
            len += blink_recr(a, memo, depth + 1)
    memo2[(num, depth)] = len
    return len

def count_digits(num):
    num = str(num)
    return len(num)

def split(num):
    num = str(num)
    return num[0 : len(num) // 2], num[len(num) // 2 :]

def count(line):
    sum = 0
    for i in line:
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        sum += blink_recr(i, memo, 0)
    return sum

print(count(l))

