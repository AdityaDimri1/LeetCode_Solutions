def findDuplicate(arr):
    # Write your code here
    ans = 0
    for i in range(len(arr)):
        ans = ans^arr[i]        # xor so we find the ans that we use for n-1 
    for i in range(1,len(arr)):
        ans = ans^i             #one by one use the ^ so that we find the duplicate value which comes twice
        print(ans) 
    return ans

print(findDuplicate([6, 3, 1, 5, 4, 3, 2]))