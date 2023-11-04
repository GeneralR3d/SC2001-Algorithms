
weights = [4, 6, 8]
profits = [7, 6, 9]
numItems = 3
capacity = 14

def knapsack(capacity,numItems):
    mem = [0]* (capacity+1)                                             # initialize 1-d dictionary of length 15(14+1)
    mem[0] = 0                                                          # base case, P(0) = 0
    for i in range(1,capacity+1):                                       # calculate from P(1)
        max = 0
        for k in range(numItems):                                       # iterate through each of the 3 items available
            if i>= weights[k] and profits[k]+mem[i-weights[k]] > max:   # if current capacity can fit the item 
                                                                        # AND the total profit from adding is > max then update max
                max = profits[k]+mem[i-weights[k]]        
        mem[i] = max                                                    # update dictionary with max value for P(i)  
    print(mem)
    return mem[capacity]

print(f"The largest total profit is {knapsack(capacity,numItems)}")
