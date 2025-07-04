def removeDuplicates(nums: list) -> int:
    if not nums:
        return 0
    
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]
    return unique_index + 1

# nums = [1, 1, 2]
# length = removeDuplicates(nums)
# print(nums[:length]) 