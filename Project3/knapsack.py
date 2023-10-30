
weights = [5, 6, 8]
profits = [7, 6, 9]
numItems = 3
capacity = 14

def knapsack(capacity,numItems):
    mem = [0]* (capacity+1)
    mem[0] = 0
    for i in range(1,capacity+1):
        max = 0
        for k in range(numItems):
            if i>= weights[k] and profits[k]+mem[i-weights[k]] > max: 
                max = profits[k]+mem[i-weights[k]]        
        mem[i] = max
    print(mem)
    return mem[capacity]

print(f"The largest total profit is {knapsack(capacity,numItems)}")
