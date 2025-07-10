def bs(nums,target):
    start = 0
    end = len(nums)-1
    mid = int((start+end)/2)
    
    while(start<=end):
        if (nums[mid]==target):
            return mid
        elif (target>nums[mid]):
            start = mid+1
        else:
            end = mid-1
        
        mid = int((start+end)/2)
        
    return start
    
bs([1,3,5,6],4)