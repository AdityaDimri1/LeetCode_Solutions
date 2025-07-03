from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

def findTriplets(arr, n, k):
    arr.sort()
    ans = set()  
    for i in range(n):
        j, l = i + 1, n - 1
        while j < l:
            total = arr[i] + arr[j] + arr[l]
            if total == k:
                ans.add((arr[i], arr[j], arr[l]))
                j += 1
                l -= 1
            elif total < k:
                j += 1
            else:
                l -= 1
    return list(ans) 
print(findTriplets([10, 5, 5, 5, 2],5,12))          