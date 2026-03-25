def hasDuplicate(nums):
    
    #using  set  0(n)
    
    num_set = set() # preffered as ideal way 
    
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False    

    
    
    # optimal using hash_map 0(n)
    
    # hash_map = {}
    
    # for num in nums:
    #     hash_map[num] = hash_map.get(num,0)+1
    #     if hash_map[num]>1:
    #         return True
    

    # for val in hash_map.values(): dont do this again this can be done easily with above loop
    #     if val > 1:
    #         return True
    
    
    # return False      
        
    
    
        
    # brute 0(n) square 2
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] == nums[j]:
    #             return True
    
    # return False        


test_cases= [
    [1, 2, 3, 3],
    [1, 2, 3, 4],
    [1,2,3,1,2,3],
    [1,2,1],
    [1]
]

for test_case in test_cases:
    print(hasDuplicate(test_case),"\n")
    


    
