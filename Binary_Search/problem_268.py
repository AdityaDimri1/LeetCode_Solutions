# def missingNumber(nums: list):
#     nums.sort()
#     for i in range(len(nums)+1):
#         if i in nums:
#             continue
#         else:
#             return i
 
# print(missingNumber([3,0,1]))

      
###===> 2nd way

# def missingNumber(nums: list):
#     for num in range(len(nums)+1):
#         if num not in nums:
#             return num
# print(missingNumber([0,3,2,1]))

####=====> 2nd method (xor method)

def missingNumber(nums: list):
    result = 0
    for num in nums:
        result ^= num
    for i in range(len(nums) + 1):
        result ^= i
    return result
        
print(missingNumber([0,3,2,1]))
