

def longestSubarray(nums,k):
    
    # using 2 pointer and left trim system but it does not works for negative numbers 
    # if the question includes noth positive and negative numbers the most 
    # optimal approach will be prefix_sum+hash_map
    
    prefix_map = {}
    
    prefix_map[0] = -1 # prefix trick always add this 
    curr_sum = 0
    max_length = 0
    
    for i in range(len(nums)):
        curr_sum+=nums[i]
        
        # if curr_sum == k: not needed
        #     max_length = i+1
        
        if curr_sum - k in prefix_map:
            max_length = max(max_length,i-prefix_map[curr_sum-k])
        
        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i    
    
    return max_length
        
    # in 2 pointer approach the max to max TC will be 0(N)
    # cause outer loop we have is already 0(n) but the inner loop is not always runnning till n
    # it only runs as much  as iterations required to reduce the curr_sum below or equals to k
    # SC - 0(1)
    
    # left = 0
    # i = 0
    # max_length = 0
    # curr_sum = 0
    # while i<len(nums):
    #     curr_sum+=nums[i]
        

    #     while curr_sum > k:
    #         curr_sum-=nums[left]
    #         left+=1
        
    #     if curr_sum == k:
    #         max_length = max(max_length,i-left+1)
            
        
    #     i+=1
   
    # return max_length         
        
        
        
    
    
    # sc - o(1) tc - o(n2)
    # max_length = 0
    
    # for i in range(len(nums)):
    #     curr_sum = 0
        # sub_max_length = 0
        
        
        # the reason why we are going till N is that lets say k is 15 and at first
        # 2 element 10+5 gave us the thing but what if lets say 10 added more 
        # it became 25 which is greator than our k but then at last we have -10 
        # and if we add that up it will give the the k as a result and longest
        # consequetive will be update from 2 to 4
        
        # for j in range(i,len(nums)):
        #     curr_sum+=nums[j]
            # sub_max_length+=1
            # Instead of maintaining sub_max_length, we can directly compute the subarray length using j - i + 1.
            # Since i is the starting index and j is the ending index, subtracting them gives the index distance, 
            # and adding 1 accounts for 0-based indexing to give the actual number of elements.
            
            # j-i+1 end_index - start_index (+1 cause its 0 index based array to get total length one added )
    #         if curr_sum == k:
    #             max_length = max(max_length,j-i+1)
    
    # return max_length            

nums = [10, 5, 2, 7, 1]
k = 15

print(longestSubarray(nums,k))


# This pattern is:

# “Subarray sum = k” → Prefix Sum + HashMap

# Can I rewrite it as:
# current_sum - previous_sum = k ?

# Think like this:

# “My current sum is too big — can I remove some earlier part to make it exactly k?”
# That “earlier part” = curr_sum - k

# formula is 
# curr_sum - k = previous_sum

# 🔥 Why we store FIRST occurrence only
# if curr_sum not in prefix_map:
#     prefix_map[curr_sum] = i

# 👉 Because:

# We want the longest subarray

# So we want:

# earliest index → maximum length

# 🔥 Final takeaway
# Prefix sum = cumulative sum
# HashMap = remembers past sums
# Logic = reverse subtraction