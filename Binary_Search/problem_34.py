def searchRange(nums: list, target: int):
    ans = []
    for i in range(len(nums)):
        if nums[i] == target:
            ans.append(i)
    if ans:
        print([ans[0], ans[-1]])
    else:
        print([-1, -1])

searchRange([5,7,7,8,8,10],6)