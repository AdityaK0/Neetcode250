


# TC-0(n) dont know just did it and it happend
def maxProfit(nums):
    profit = 0
    previous_price = nums[0]
    for i in range(1,len(nums)):
        
        if nums[i]<previous_price:
            previous_price = nums[i]
            # “Why would I buy at 7? I’ll buy at 1 instead.”
        else:
            profit+=nums[i]-previous_price
            previous_price = nums[i]    
    
    return profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))


# logic behind this says is that why would i buy the stock
# if next day the stock price will go down instead of this 
# let me purchase on the next day when it will be low
# so i sold at the same day then bought the other next day 
# by updating the previous_price