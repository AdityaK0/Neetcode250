def longestConsecutive(nums):
    
    # using set  TC - 0(n) SC - 0(n)
    
    nums_set = set(nums)
    max_length = 0
    for num in nums:
        sub_length = 0
        if num-1 not in nums_set:
            
            # the reason behind this num+sub_length is that it will check it self too in set which will be 
            # counted in longest sequence length 
            while num+sub_length in nums_set:
                sub_length+=1
                
            max_length = max(max_length,sub_length)
    
    return max_length
    
    
    # TC - 0(n * nlog n) SC - 0(n)
    
    
    # sorted_nums = sorted(nums) 
    
    # max_consicutive = 0
    # sub_max = 1
    # for i in range(1,len(sorted_nums)):
    #     if sorted_nums[i] - sorted_nums[i-1] == 1:
    #         sub_max+=1
    #     elif sorted_nums[i] - sorted_nums[i-1] == 0:
    #         pass
    #     else:
    #         max_consicutive = max(sub_max,max_consicutive)
    #         sub_max = 1
    
    # return max(max_consicutive,sub_max)    
    
               
            
            
        
        




print(longestConsecutive([2,20,4,10,3,4,5]))
print(longestConsecutive([0,3,2,5,4,6,1,1]))

