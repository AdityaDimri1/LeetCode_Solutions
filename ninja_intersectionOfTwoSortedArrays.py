from os import *
from sys import *
from collections import *
from math import *

def findArrayIntersection(arr: list, brr: list):
    store = []
    i, j = 0, 0 
    while i < len(arr) and j < len(brr):
        if arr[i] < brr[j]:
            i += 1  
        elif arr[i] > brr[j]:
            j += 1  
        else:
            store.append(arr[i])  
            i += 1
            j += 1  
    return store

print(findArrayIntersection([1, 2, 2, 2, 3, 4], [2, 2, 3, 3]))