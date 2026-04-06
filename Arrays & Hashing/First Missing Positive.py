def firstMissingPositive(nums):
    
    # most optimized without using 0(n) Space
    
    
    # another parts comes is that we can also solve this without sorting 
    # as we know the the answer will always between nums[0] to len(nums)+1  len(nums)+1 this as a last element
    
    hashSet = [0]* (len(nums)+1)
    
    for i in range(len(nums)):
        if not nums[i]>len(nums):
           hashSet [nums[i]-1] = nums[i]
       
    curr_postive_number = 1
    for i in range(len(hashSet)):
        if hashSet[i] == curr_postive_number:
            curr_postive_number+=1
    
    return curr_postive_number        
    
    
    
    
    # need to find the smallest positive missing number 
    # in general smallest positive number is 1 so we one solution came to to mind is that 
    # while iterating we need to find the smallest missing positive number 
    # and if that smallest positive already there in the array means this one is not the missing one
    # and if nothing matches which means the element is not from the array 
    # to implement and check from smallest to largest we need to sort the array
    
    # sorted_nums = sorted(nums)
    # smalles_positive_number = 1
    # i = 0
    # while i<len(sorted_nums):
    #     if smalles_positive_number == sorted_nums[i]:
    #         smalles_positive_number+=1 # as we already have the element in the array
    #                                    # which means now need to find the next positive number
    #     i+=1
    # return smalles_positive_number                                   


print(firstMissingPositive([-2,-1,0]))
print(firstMissingPositive([1,2,4]))
print(firstMissingPositive([1,2,4,5,6,3,1]))
print(firstMissingPositive([7,8,9,11,12]))
