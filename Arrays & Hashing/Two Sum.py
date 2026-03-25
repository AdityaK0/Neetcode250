
def twoSum(nums,target):
    
    
    # optimal using hash_map differentiation things
    # ⏱️ Complexity
    # Time: O(n)
    # Each lookup in hashmap → O(1)
    # Loop runs n times
    # Space: O(n)
    # In worst case, store all elements
    
    hash_map = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in hash_map:
            return [hash_map[diff],i]
        hash_map[nums[i]] = i
    
    
    
    
    #brute Time: O(n²). Space : O(1) For each element, check all others
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

test_cases = [
    
    [[3,4,5,6],7],
    [[4,5,5,6],10],
    [[5,5],10]
]

for test in test_cases:
    print(twoSum(test[0],test[1]))