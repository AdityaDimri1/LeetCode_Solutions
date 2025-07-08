####=============================> Binary Search logic understanding 

def bs(arr, key, size):
    start = 0                       #1st part of the array
    end = size-1                    #2nd part of the array
    mid = int((start + end)/2)      #create the mid which seprate array in two part
    
    while(start<=end):              
        if (arr[mid]==key):         #if value match then written the key location
            return mid
        
        if (key>arr[mid]):          #if value is grater then mid then update the start value
            start = mid+1
        else:                       #if not the update the end value 
            end = mid-1
        mid = int((start + end)/2)    #update the mid when in first iteration the valuie not match
        
    return -1                       #if the key value not in the array

print(bs([1,2,3,4,5,6],2,6))
