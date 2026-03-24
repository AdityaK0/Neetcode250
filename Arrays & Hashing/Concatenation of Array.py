def getConcatenation(nums):
    # return nums+nums
    new_array = []
    for num in nums:
        new_array.append(num)
    
    for num in new_array:
        nums.append(num)
    
    return nums        

print(getConcatenation([22,21,20,1]))

