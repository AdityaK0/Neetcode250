# its basically like take the current_price if the next is at low 
# then sell at the same and buy at the next day so here
# we have to do the same right here 


def maxProfit(prices):
    
    curr_price = prices[0]
    max_profit = 0
    # if question says find profit and loss at each step then this solution 
    # of curr_profit will be used 
    # Version 1 is not just for this problem.

    # It is a pattern:

    # answer = max(answer, current - best_so_far)
    # best_so_far = min(best_so_far, current)
        
    for i in range(1,len(prices)): # trackes price at each buy and sell
        
        curr_profit = prices[i] - curr_price
        max_profit = max(curr_profit,max_profit)
        curr_price = min(curr_price,prices[i])
    
    
    
    bought_at_price = prices[0]
    max_profit = 0
    
    
    # tracks price only when getting profit
    # You skip negative profit cases entirely
    for i in range(1,len(prices)):
        if bought_at_price>prices[i]: 
            # like 7>1 then sell at the same day when we bought at 7 and buy again next_day
            bought_at_price = prices[i]
        else:
            # its obvious that next day we have high profit and the next day stock price
            # is more the will sell and  update the max_profit
            max_profit = max(max_profit,prices[i]-bought_at_price)
    
    return max_profit

print(maxProfit([7,1,5,3,6,4]))  
print(maxProfit([7,6,4,3,1]))            
          
        