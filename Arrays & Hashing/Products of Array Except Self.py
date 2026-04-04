def productExceptSelf(nums):
    
    # ideal way is that create suffix and prefix of the element and multiply
    # suffix and prefix of the element you will get the product of the element expect it self
    
    
    # here in 0(n) Space we got the value 
    prefix = [0]*len(nums)
    prefix[0] = 1
    
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1]*nums[i-1]
    
    right = 1
    
    for i in range(len(nums)-1,-1,-1):
        prefix[i] = prefix[i]*right
        right*=nums[i]
    return prefix
    
    
    # suffix = [0]*len(nums)
    # suffix[-1] = 1
    
    # for i in range(len(nums)-2,-1,-1):
    #     suffix[i] = suffix[i+1]*nums[i+1]
    
    # res = [] 
    
    # for i in range(len(nums)):
    #     res.append(prefix[i]*suffix[i])
    
    return res        
    
    
    
    
    
    # curr_index = 0 takes 0(n2)
    
    # res = []
    
    # while curr_index<len(nums):
        
    #     curr_index_product = 1
        
    #     curr_index_after = curr_index+1
        
    #     while curr_index_after<len(nums):
    #         curr_index_product*=nums[curr_index_after]
    #         curr_index_after+=1
        
    #     curr_index_before = curr_index-1
        
    #     while curr_index_before>-1:
    #         curr_index_product*=nums[curr_index_before] 
    #         curr_index_before-=1
        
    #     res.append(curr_index_product)
        
    #     curr_index+=1
    
    # return res            


print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,0,1,2,3]))



# ---

# ## Solution 1 (Your approach: Prefix + running suffix in one array)

# ```python
# prefix = [0]*len(nums)
# prefix[0] = 1

# for i in range(1,len(nums)):
#     prefix[i] = prefix[i-1]*nums[i-1]

# right = 1

# for i in range(len(nums)-1,-1,-1):
#     prefix[i] = prefix[i]*right
#     right*=nums[i]
# ```

# ---

# ### TC - O(n)

# Detailed why

# Break into phases:

# 1. First loop (prefix):

# * Runs `n-1` times
# * Constant work each time
#   → O(n)

# 2. Second loop (suffix using `right`):

# * Runs `n` times
# * Constant work each time
#   → O(n)

# Total:

# ```
# O(n) + O(n) = O(n)
# ```

# No nested loops, each element processed constant number of times.

# ---

# ### SC - O(1) (important)

# Detailed why

# * Output array (`prefix`) is **not counted** (interview rule)
# * Only extra variable used → `right`

# So:

# ```
# Extra space = O(1)
# ```

# ---

# ### Why this works

# For each index:

# ```
# answer[i] = (product of left elements) * (product of right elements)
# ```

# You compute:

# * Left product → stored in `prefix`
# * Right product → maintained using `right`

# ---

# ## Solution 2 (Prefix + Suffix arrays)

# TC - O(n)
# SC - O(n)

# Why

# * Two extra arrays (`prefix`, `suffix`)
# * Each loop is linear, but extra space used

# ---

# ## Solution 3 (Brute force)

# TC - O(n²)
# SC - O(1)

# Why

# * For each index → traverse entire array again

# ---

# ## Follow-up: “Without using division”

# ### What is the division solution?

# ```python
# total_product = 1
# for num in nums:
#     total_product *= num

# res = []
# for num in nums:
#     res.append(total_product // num)
# ```

# ---

# ### TC - O(n)

# ### SC - O(1)

# ---

# ### Why division is NOT allowed

# Because of **zero problem**:

# Example:

# ```
# nums = [1,2,0,4]
# ```

# * total_product = 0
# * Now:

# ```
# res = [0/1, 0/2, 0/0, 0/4]  → division by zero error
# ```

# Also:

# * If more than one zero → everything becomes 0
# * Needs special handling → messy logic

# ---

# ### Why your approach is better

# * Handles zeros naturally
# * No division edge cases
# * Cleaner logic
# * Industry-preferred solution

# ---

# ## Final evaluation of your solution

# * Correctness: correct
# * Optimality: optimal (O(n), O(1))
# * Approach: standard interview solution
# * Understanding: solid

# ---

# ## Short summary (as you want)

# ### Solution 1 (Your approach)

# TC - O(n)
# SC - O(1)
# Why
# Two linear passes. Uses output array + one variable. No extra space.

# ---

# ### Solution 2 (Prefix + Suffix arrays)

# TC - O(n)
# SC - O(n)
# Why
# Uses two extra arrays for left and right products.

# ---

# ### Solution 3 (Division)

# TC - O(n)
# SC - O(1)
# Why
# Uses total product, but fails with zeros → not allowed.
