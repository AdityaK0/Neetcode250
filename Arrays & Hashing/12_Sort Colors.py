
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    # optimized way is using the Dutch national flag algorithm
    # basically push the bigger value at right and smaller at left at the end one will remain at center 
    
    
    # When we find a 2 at index i, we swap it with the element at the right.
    # But we do not increment i because the swapped element might also be 2 or some other value. 
    # Since we haven’t processed it yet, we need to check it again in the next iteration
    
    # situation  : 
    
    # Suppose nums[i] == 2 and nums[right] is also 2
    # After swapping, the array remains the same (2 swapped with 2)
    # If we increment i, we would skip this position, leaving the 2 incorrectly placed

    # Instead:

    # We decrease right
    # Keep i the same
    # Re-check the new value at index i
    
    # [1, 0, 1, 2, 1, 2]
    #         ↑ i
    # Found 2 → swap with right
    # Right might also have 2 or some other value
    # We don’t know yet, so we must check again
    
    left = 0
    right = len(nums)-1
    i = 0
    while i<=right: # why this is not len(nums) because len(nums) will go for all elements  which we dont want what if some of that 
                    # part is already sorted so will go till right only 
        
        if nums[i] == 0:
            nums[left],nums[i] = nums[i],nums[left]
            left+=1
            i+=1
        elif nums[i] == 2:
            nums[right],nums[i] = nums[i],nums[right]
            right-=1
        else:
            i+=1
    
    return nums                            
        
    
    
    
    
    

    # below i was using 0(n) array as space here im using 0(1) but 2 iteration
    # red,white,blue = 0,0,0
    
    # for num in nums:
    #     if num==0:
    #         red+=1
    #     elif num==1:
    #         white+=1
    #     else:
    #         blue+=1
    
    # i = 0

    # while red:
    #     nums[i] = 0
    #     red-=1
    #     i+=1

    # while white:
    #     nums[i] = 1
    #     white-=1
    #     i+=1

    # while blue:
    #     nums[i] = 2
    #     blue-=1
    #     i+=1

    




    # red,white,blue = [],[],[]

    # for num in nums:
    #     if num==0:
    #         red.append(num)
    #     elif num==1:
    #         white.append(num)   
    #     else:
    #         blue.append(num)     
    # combo = red+white+blue

    # for i in range(len(combo)):
    #     nums[i] = combo[i]

    # return nums    


print(sortColors([1,0,1,2])) #[0,1,1,2]