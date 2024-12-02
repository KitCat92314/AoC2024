import numpy as np
import pandas as pd

nums = open("Day2.txt", "r")
rows = []
for i in nums:
    row = i.split()
    for j in range(len(row)):
        row[j] = int(row[j])
    rows.append(row)

def safety(matrix):
    safes = 0
    for i in matrix:
        sort = i.copy()
        sort.sort()
        rev = i.copy()
        rev.sort(reverse=True)
        if i == sort or i == rev:
            save = True
            for j in range(len(i) - 1):
                if abs(i[j + 1] - i[j]) > 3 or abs(i[j + 1] - i[j]) < 1:
                    save = remove1(i)
                    break
            if save:
                safes += 1
        else: 
            if(remove1(i)): safes += 1
    return safes

def remove1(unsafe):
    
    for i in range(len(unsafe)):
        temp = unsafe.copy()
        temp.pop(i)
        sort = temp.copy()
        sort.sort()
        rev = temp.copy()
        rev.sort(reverse=True)
        if temp == sort or temp == rev:
            saved = True
            for j in range(len(temp) - 1):
                if abs(temp[j + 1] - temp[j]) > 3 or abs(temp[j + 1] - temp[j]) < 1:
                    saved = False
                    break
            if saved: return True   
    return False

print(safety(rows))
