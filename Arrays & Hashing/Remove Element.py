
def removeElement(nums,val):
    # Fast & Slow Pointer (Filtering)

    # using normal loop but in this it does not shit val on the last side 
    k = 0
    for i in range(len(nums)):
        if nums[i]!=val:
            # nums[k] = nums[i] # if no need to to push back the element this this is good else swap the element 
            nums[k],nums[i] = nums[i],nums[k]
            k+=1
    return nums,k        
            
                  
    
    # if not nums : # maintains order and push back the element too
                    # or len(nums)==1 removed this part from here cause even if i came but it does not equals to then it 
                    # will be counted as that yes it does not equals to that  
    #     return i
    
    # while i<len(nums) and nums[i]!=val:
    #     i+=1
    
    # if not i<len(nums) or i == len(nums)-1:
    #     return i
    
    # j = 0
    # if i<len(nums)-1:
    #     j = i+1
        
    # while j<len(nums):
    #     if nums[j] != val:
    #         nums[i],nums[j] = nums[j],nums[i]
    #         i+=1
    #         j+=1
        
    #     else:
    #         j+=1
    # return nums          
               
        
    
          



nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums,val))
print(removeElement([1,1,2,3,4],1))
print(removeElement([],10))
print(removeElement([1],2))
print(removeElement([2,1],2))
print(removeElement([4,5,6,7,8],9))

# basically need to update the place where 1 is available from its next very element 




### Solution 1 (Two Pointer / In-place Filtering)

# TC - O(n)
# SC - O(1)

# Why
# Single pass through array. Each element checked once. Swap/write valid elements to front using pointer `k`. No extra space used.

# Algorithm
# Two Pointer (Fast & Slow)

# ---

# ### Note (important)

# * Order is **not guaranteed** because of swapping:

# ```python
# nums[k], nums[i] = nums[i], nums[k]
# ```

# If order matters, use:

# ```python
# nums[k] = nums[i]
# ```

# ---

# ### Solution 2 (Stable version – maintain order)

# TC - O(n)
# SC - O(1)

# Why
# Same traversal, but instead of swapping, overwrite positions. Keeps relative order of elements.

# Algorithm
# Two Pointer (Stable Write)