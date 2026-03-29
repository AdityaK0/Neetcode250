
from re import L


def merge(nums1,nums2):
    pass


def divide(nums,left,right):
    if not left<=right:
        return nums
    mid = (left+right)//2
    
    return divide(nums,left,mid)+divide(nums,mid+1,right)    
    



def sortArray(nums):
    divide(nums,0,len(nums))
    pass



print(sortArray([23,12,4,2,34,2,4511,11,78]))