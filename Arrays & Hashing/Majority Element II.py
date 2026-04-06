
# need to return 2 majorly repeated element from the given array

# the question does not means major element at least 2
# questions asks the element appear more than n//3 times 

# example len(nums) is 10 and 10//3 = 3 element appearing more than 3 time 4 or 5 times 



# Extended Boyer–Moore Voting Algorithm (for n/3 case)  
# If 3 elements each appear > n/3 → total > n → impossible


def majorityElement(nums):
    
    candidate1 = None
    candidate2 = None # initialized with none cause if 0 will be in arr then it can increase the count can lead to mismatch count 
    count1 = 0
    count2 = 0
    
    for i in range(len(nums)):
        if nums[i] == candidate1:
            count1+=1
        elif nums[i] == candidate2:
            count2+=1
        elif count1 == 0:
            candidate1 = nums[i]
            count1 = 1
        elif count2 == 0:
            candidate2 = nums[i]
            count2 = 1
        else:
            count1-=1
            count2-=1
    bound  = len(nums)//3
    
    
    # instead of 2 times using .count() we can calculate the count in one pass too
    count1 = 0 # this look much just to count the candidate count but if the array has 
               # 1 million length then calculation both in one pass would be an better idea
    count2 = 0 

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    res = [] 
    if count1>bound:
        res.append(candidate1)
    if count2>bound:
        res.append(candidate2)    
    
    return res                     
    
    # need to do this in 0(1) space complexity
    
    # hash_map = {}
    # for num in nums:
    #     hash_map[num] = hash_map.get(num,0)+1
    
    # bound  = len(nums)//3
    
    # res = []
    
    # for key,val in hash_map.items():
    #     if val>bound:
    #         res.append(key)
    
    # return res        
               


print(majorityElement([5,2,3,2,2,2,2,5,5,5]))
print(majorityElement([4,4,4,4,4]))
print(majorityElement([1,2,3]))
print(majorityElement([1,1,1,3,3,2,2,2]))


