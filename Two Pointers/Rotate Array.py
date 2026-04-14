def rotate(nums,k):
    
    temp = []
    n = len(nums)
    
    k = k%n
    
    for i in range(n-k,n,1):
        temp.append(nums[i])
    
    for i in range(n-k):
        temp.append(nums[i])    
    
    return temp    
    
    # for i in range(k):
    #     temp.append(nums[n-i])
    
    # for i in range(0,n-k+1,1):
    #     temp.append(nums[i])
        
    # for i in range(len(temp)):
    #     nums[i] = temp[i]
        
    # return nums   
    


print(rotate([1,2,3,4,5,6,7,8],4))
print(rotate([1,2,3,4,5,6,7],3))
print(rotate([1,2,3,4,5,6,7],300))


