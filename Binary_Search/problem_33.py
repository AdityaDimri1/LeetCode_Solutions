def search(nums: list, target: int):
    for i in range(len(nums)):
        if (nums[i]==target):
            return i
    return -1

print(search([4,5,6,7,0,1,2],0))
print(search([4,5,6,7,0,1,2],3))
print(search([1],1))