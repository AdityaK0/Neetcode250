def threeSome(nums):
    
    # optimal 
    
    result = []
    nums = sorted(nums)
    
    for i in range(len(nums)):
        if i!=0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = len(nums)-1
        
        while j<k:
            total = nums[i]+nums[j]+nums[k]
            
            if total>0:
                k-=1
            elif total<0:
                j+=1
            else:
                result.append([nums[i],nums[j],nums[k]])
                k-=1
                j+=1
                
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                
                while j>k and nums[k]==nums[k-1]:
                    k-=1  
    
    return result                                         
    
    
    
    # brute force with skip duplicate series
    # result = []
    # nums = sorted(nums)
    # for i in range(len(nums)):
    #     if i!=0 and nums[i] == nums[i-1]:
    #         continue
        
    #     for j in range(i+1,len(nums)):
    #         if j>i+1 and nums[j] == nums[j-1]:
    #             continue
    #         for k in range(j+1,len(nums)):
    #             if k>j+1 and nums[k] == nums[k-1]:
    #                 continue
    #             if nums[i]+nums[j]+nums[k] == 0:
    #                 result.append([nums[i],nums[j],nums[k]])
    
    # return result                
                    


print(threeSome([-1,0,1,2,-1,-4]))