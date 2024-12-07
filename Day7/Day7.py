import re
values = []
file = open("Day7.txt", "r")
for i in file:
    nums = re.findall("[0-9]+", i)
    temp = []
    for j in nums:
        temp.append(int(j))
    values.append(temp)

def test_num(values):
    return any([_test_num_mul(values, 1, values[1]), _test_num_add(values, 1, values[1]), _test_num_together(values, 1, values[1])])

def _test_num_mul(values, idx, amount):
    if idx + 1 < len(values):
        return any([_test_num_mul(values, idx + 1, amount * values[idx + 1]), _test_num_add(values, idx + 1, amount * values[idx  + 1]), _test_num_together(values, idx + 1, amount * values[idx  + 1])])
    else: return amount == values[0]

def _test_num_add(values, idx, amount):
    if idx + 1 < len(values):
        return any([_test_num_mul(values, idx + 1, amount + values[idx + 1]), _test_num_add(values, idx + 1, amount + values[idx  + 1]), _test_num_together(values, idx + 1, amount + values[idx  + 1])])
    else: return amount == values[0]

def _test_num_together(values, idx, amount):
    if idx + 1 < len(values):
        amount = int(str(amount) + str(values[idx + 1]))
        return any([_test_num_mul(values, idx + 1, amount), _test_num_add(values, idx + 1, amount), _test_num_together(values, idx + 1, amount)])
    else: return amount == values[0]

def sum(lines):
    sum = 0
    for i in lines:
        if test_num(i):
            sum += i[0]
    print(sum)

sum(values)

