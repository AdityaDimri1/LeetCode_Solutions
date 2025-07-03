from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    ans = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == s:
                ans.append((arr[i], arr[j]))
    return ans
            
print(pairSum([2, -3, 3, 3, -2],0))