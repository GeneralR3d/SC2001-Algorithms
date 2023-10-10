- unidirectional and bidirectional doesnt seem to affect time complexity
- When V are small, list seem to do better than matrix which is what we expect, and looks like the gap will diverge
- When V gets larger, list still seems to always do better than matrix but the gap does not seem to diverge, they seem to follow a similar time complexity
- Even though in theoretical analysis (V+E)logV seems to be worse than V^2
- But chatGPT tells us its about the same, so we have to change theoretical time complexity analysis

-TAKE NOTE:
- to implement priorityq as an array, using a list then always sorting it is stupid, since the sort itself takes nlgn time. Since each time we are only concerned with finding the minimum value in the array, a simple linear search of O(n) would be less expensive than maintaining a sorted array each time we add a element to it
- PYTHON BUILT IN FUNCTIONS ARE EXPENSIVE, list.pop(index) is actually O(n), so it cannot be used as a constant time removal of any element


2 ways of writing dijkstra

1. create empty priority queue like we did here, only add nodes to priority queue, ie let nodes be the frontier if they are not visited AND the newcost which is currentCost to get to node + weight is LESSER than the existing cost. 
    - Downside is we need to create an additional distance array and init to inifity at the start, to store all our current best estimates to get to
    
2. create a priority and IMMEDIATELY add all nodes to the queue, before starting the search, this way all the nodes are automatically in frontier, and are always sorted by their distance. This way we DONT need an additional distance array.