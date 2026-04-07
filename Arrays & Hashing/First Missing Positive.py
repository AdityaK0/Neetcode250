def firstMissingPositive(nums):
    
    
    # another solution which i saw mostly used on leetcode was place nums[i] at its correct place
    # then iterate and find the it is index based + 1 sorted or not if not then its the ans 
    #Cyclic Sort / Index Placement
    
    #“If a number x exists, put it at index x-1.”
    n = len(nums)
    for i in range(len(nums)):
        while 1<=nums[i]<=n and nums[i] != nums[nums[i]-1]:
            correct_index = nums[i]-1
            nums[correct_index],nums[i] = nums[i],nums[correct_index]
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    
    return n+1    
                    
    # Algorithm
    # Index marking / cyclic presence tracking
    
    # 1 : eliminating while tracking if 1 is present or not
    
    is_1_present = False
    
    for i in range(len(nums)):
        if nums[i] == 1:
            is_1_present = True
        elif nums[i]<1 or nums[i]>len(nums):
            nums[i] = 1
    
    if not is_1_present:
        return 1 # as we are marking non eligible element as one so it is also need to find that even 1 also exists or not
    
    # implement negation on each element to mark their presence 
    
    # for i in range(len(nums)):
    #     num = abs(nums[i]) # if the value is already negative then how we are suppose to find it index 
    #     index = num-1      # to find the index we have to do num - 1 to get index and if it is already 
    #                        # negative number then its not possible so need the abs value 
        
    #     if nums[index]<0: # if the mark is already done then not need to mark it again 
    #         continue # you can skip this step but it show how to improve idempotency
        
    #     nums[index]*=-1
    
    for i in range(len(nums)):
        num = abs(nums[i])
        index = num-1
        
        if not nums[index]<0:
            nums[index] = nums[index]*-1
        
    
    # find the positive number 
    
    for i in range(len(nums)):
        if nums[i]>0:
            return i+1
    
    return len(nums)+1       
    

            
                
    
    
    
    # most optimized without using 0(n) Space
    # here we have to use the input array as 
    
    # steps to solve this with 0(1) Space Complexity
    
    # first the questions says we need to find the elements who are smallest 
    # positive numbers which means numbers<1 and greator then len(nums) are not eligible as smallest positive number
    
    # so we will eliminate them while putting 1 at thier place as we put at each non-eligible positive number
    # so we will also track first even one is available or not 
    
    # why we are tracking it is the part of second step when we convert each element into negative number
    # to convert it into negative will do element-1 = got index make that index as negative which will
    # tell us that yes this element exists so in the previous step when we were marking the
    # non-eligible element 1 so if we were not tracking if 1 is available or not then it would have 
    # been marked 1 as available even though it was not 
    
    # at last step will iterate find if the number > 0 then it the ans 
    # while iteration if nothing found means ans is n+1
    
    
    
        
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


### Solution 1 (Optimal in-place marking)

# TC - O(n)
# SC - O(1)

# Why

# * Step 1: clean invalid numbers → O(n)
# * Step 2: mark presence using index (negation) → O(n)
# * Step 3: find first positive index → O(n)
# * Total = 3 passes → O(n)
# * No extra data structures used, only input array modified → O(1)

# Algorithm
# Index marking / cyclic presence tracking

# ---

# ### Solution 2 (Your hash array approach)

# TC - O(n)
# SC - O(n)

# Why

# * First loop fills hash array → O(n)
# * Second loop finds missing number → O(n)
# * Extra array of size n+1 used → O(n) space

# Algorithm
# Hashing / presence array

# ---

# ### Solution 3 (Sorting)

# TC - O(n log n)
# SC - O(1) or O(n) (depends on sorting)

# Why

# * Sorting dominates → O(n log n)
# * Single pass after sorting → O(n)
# * Space depends on sorting implementation

# Algorithm
# Sorting

# ---

# ### Key Insight

# * Answer always lies in range:

# ```
# 1 to n+1
# ```

# * Optimal solution uses:

# ```
# value → index mapping
# ```

# ---

# ### Final note (important)

# Your understanding of optimal solution is correct:

# * Ignoring invalid numbers
# * Using index as marker
# * Tracking presence via sign

# That’s exactly how top solutions work.
