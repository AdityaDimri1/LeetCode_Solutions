#==================================> 1st logical way 
from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    left = m+1
    right = len(arr)-1
    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
        
    return arr
print(reverseArray([1, 2, 3, 4, 5, 6],3))

##=================================> 2nd and simple way

# from os import *
# from sys import *
# from collections import *
# from math import *

# def reverseArray(arr, m):
#     arr[m+1:] = reversed(arr[m+1:])
#     return arr
# print(reverseArray([1, 2, 3, 4, 5, 6],3))
        