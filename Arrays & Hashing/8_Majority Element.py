

# Boyer–Moore Voting Algorithm says that reset the current value once it reaches 0 with the current iteratin element 

# remember the name Boyer–Moore Voting Algorithm
def majorityElement(nums):
    res = nums[0]
    ctn = 1
    for i in range(1,len(nums)):
        if res == nums[i]:
            ctn+=1
        elif ctn == 0:
            res = nums[i]
            ctn = 1    
        else:
            ctn-=1    
    return res
    
    # maxCount  = 0
    # count  = {}
    # res = nums[0]
    # for num in nums:
    #     count[num] = count.get(num,0)+1
    #     res  = num if count[num]>maxCount else res
    #     maxCount = max(maxCount,count[num])
        
    # return maxCount,res


print(majorityElement([5,5,1,1,1,5,5]))




# Solution 1 (Boyer–Moore Voting Algorithm)

# TC - O(n)
# SC - O(1)

# Why
# Single pass through array. Count increases/decreases to cancel out non-majority elements. Majority element remains at the end. No extra space used.

# Algorithm
# Boyer–Moore Voting Algorithm

# Solution 2 (Hash Map / Counting)

# TC - O(n)
# SC - O(n)

# Why
# Traverse array and store frequency of each element in dictionary. Majority element will have count > n/2. Extra space used for storing counts.