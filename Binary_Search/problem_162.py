def findPeakElement(nums: list):
    val = 0
    for i in range(len(nums)):
        if nums[i] >= nums[i-1]:
            val = i
        else:
            continue 
    print(val)
findPeakElement([1,2,1,3,5,6,4])
findPeakElement([2,1])