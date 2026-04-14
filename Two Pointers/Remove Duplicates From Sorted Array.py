def removeDuplicates(nums):
    
    # instead of removing just update the array 
    ele = nums[0]
    pos = 1
    for i in range(1,len(nums)):
        if nums[i]!=ele:
            nums[pos] = nums[i]
            ele = nums[i]
            pos+=1

    return pos   
    # lastOccuredElement = nums[0]
    # k = 1
    # j = 1
    # n = len(nums)
    
    # while j<n:
        
    #     if nums[j] == lastOccuredElement:
    #         nums[j] = -1000
    #         j+=1
    #     else:
    #         lastOccuredElement =  nums[j]   
    #         k+=1
    #         j+=1 
    
    # while n:
    #     if nums[n-1] == -1000:
    #         nums.pop(n-1)
    #     n-=1
    
    # return nums,k


print(removeDuplicates([1,1,2,3,4]))
print(removeDuplicates([2,10,10,30,30,30]))
print(removeDuplicates([2]))

