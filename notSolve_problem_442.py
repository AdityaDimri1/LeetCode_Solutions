#======================================> simple way solution
# class Solution:
#     def findDuplicates(self, nums: list):
#         unique = []
#         count = []
#         for num in nums:
#             if num not in unique:
#                 unique.append(num)
#             else:
#                 count.append(num)
#         return count  
# solution = Solution()
# print(solution.findDuplicates([4,3,2,7,8,2,3,1]))


##======================================> 2nd approach
# class Solution:
#     def findDuplicates(self, nums: list):
#         nums.sort()
#         count = []
#         i = 0
#         for i in range(len(nums)):
#             if nums[i] in nums[:i]:
#                 count.append(nums[i])
#         return count
# solution = Solution()
# print(solution.findDuplicates([4,3,2,7,8,2,3,1]))


##=======================================> 3rd approach
class Solution:
    def findDuplicates(self, nums: list):
        if len(nums) == 1:
            return []
        
solution = Solution()
print(solution.findDuplicates([4,3,2,7,8,2,3,1]))