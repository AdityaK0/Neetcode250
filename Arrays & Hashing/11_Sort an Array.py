


# will do this in sorting all together things 

def merge(nums,left,right,mid):
    while left>=right:
        return


def divide(nums,left,right):
    if left>=right:
        return nums
    mid = (left+right)//2
    
    divide(nums,left,mid)
    divide(nums,mid+1,right)    
    merge(nums,left,right,mid)
    



def sortArray(nums):
    divide(nums,0,len(nums))
    pass



print(sortArray([23,12,4,2,34,2,4511,11,78]))