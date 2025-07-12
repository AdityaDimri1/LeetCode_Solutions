##=======> 1st method 

# def intersection(nums1: list, nums2: list):
#     instersect = []
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums1[i] not in instersect:
#                 if nums1[i]==nums2[j]:
#                     instersect.append(nums1[i])
#                 else:
#                     continue
#             else:
#                 continue
#     return instersect   
        
# print(intersection([4,9,5],[9,4,9,8,4]))



###====>  2nd method (using set and and operater)

def intersection(nums1: list, nums2: list): 
    return list(set(nums1) & set(nums2))

print(intersection([4,9,5],[9,4,9,8,4]))

