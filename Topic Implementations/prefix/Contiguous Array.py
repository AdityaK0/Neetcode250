

def findMaxLength(nums):
    # for i in range(len(nums)):
    #     if nums[i] == 0:  
    #         nums[i] = -1
     
      
      
    # FOLLOW UP QUESTION WHAT IF ASKED FIND IN 2:1 WHICH MEANS 1 count 2 twice of 0 count 
    prefixMap = {0:-1}
    maxLength = 0
    curr_sum = 0
    
    for i in range(len(nums)):
        curr_sum+= 1 if nums[i] ==1 else -1
        
        if curr_sum in prefixMap:
            maxLength = max(maxLength,i-prefixMap[curr_sum])
        else:   
            prefixMap[curr_sum] = i
    
    return maxLength

print(findMaxLength([0,1]))
print(findMaxLength([0,1,0]))
print(findMaxLength([0,1,1,1,1,1,0,0,0]))
print(findMaxLength([1,0,1,0,1,0,1]))
print(findMaxLength([0,1,1,0,1,1,1,0]))


