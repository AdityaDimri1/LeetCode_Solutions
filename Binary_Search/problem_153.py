def findMin(nums: list):
    val = nums[0]
    for i in range(1,len(nums)):
        if val > nums[i]:
            val = nums[i]
        else:
            continue
    print(val)

findMin([11,13,15,17])