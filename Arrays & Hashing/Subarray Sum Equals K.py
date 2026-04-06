
def subarraySum(nums,k):
    
    prefixMap = {0:1}
    curr_sum = 0
    subArrayPossibilityCount = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        subArrayPossibilityCount+=prefixMap.get(curr_sum-k,0)
        prefixMap[curr_sum] = prefixMap.get(curr_sum,0)+1
    
    return subArrayPossibilityCount    
        
        
    
    # for i in range(len(nums)):
    #     curr_sum+=nums[i]
        
    #     if curr_sum - k in prefixMap:
    #         subArrayPossibilityCount+=prefixMap[curr_sum-k]
        
        
    #     # incremented cause if the current_sum again comes to the element which is present in
    #     # the prefix that means increase the count so next it will appear the count is incresed
    #     # will plus that in the possibility count
        
    #     if curr_sum not in prefixMap:
    #         prefixMap[curr_sum] = 1
    #     else:
    #         prefixMap[curr_sum]+=1    
    
    # return subArrayPossibilityCount          
            
              
            

nums =  [10, 5, 2, 7, 1, -10]
k = 15

# nums = [1,2,3]
# k = 3

print(subarraySum(nums,k))