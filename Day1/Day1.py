import numpy as np
import pandas as pd

def list_diff(left, right):
    sum = 0
    left.sort()
    right.sort()
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum

def list_similar(left, right):
    sum = 0
    left.sort()
    right.sort()
    for i in left:
        sames = 0
        for j in right:
            if i == j:
                sames += 1
        sum += i * sames
    return sum


data = pd.read_csv("Day1.csv", sep="   ", header=None)
print(list_diff(data[0].to_list(), data[1].to_list()))
print(list_similar(data[0].to_list(), data[1].to_list()))