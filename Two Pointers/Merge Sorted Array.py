
def merge(nums1,m,nums2,n):
    
    
    # depends on how you fill the nums1 as if both nums1 and nums2 are sorted then
    # then there is 100% chance that either m-1 index on nums1 or n-1 index of nums2 contains the 
    # largest element so in this way will sort from back and at last will
    # will add the remaining part 
    p2 = n-1
    p1 = m-1
    
    p = (m+n) - 1
    
    
    while p1>=0 and p2>=0:
        
        if nums2[p2]>nums1[p1]:
            nums1[p] = nums2[p2]
            p2-=1
            p-=1
        else:
            nums1[p] = nums1[p1]
            p1-=1
            p-=1
    
    while p1>=0:
        nums1[p] = nums1[p1]
        p1-=1
        p-=1
    
    while p2>=0:
        nums1[p] = nums2[p2]
        p2-=1
        p-=1
    
    return nums1                 
    
    # for k in range(n):
    #     nums1[m+k] = nums2[k]
    
    # return sorted(nums1)
             
print(merge([10,20,20,40,0,0],4,[1,2],2))
print(merge([0,0],0,[1,2],2))
print(merge([1,2,3,0,0,0],3,[2,5,6],3))

