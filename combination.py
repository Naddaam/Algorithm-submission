def combinations(n, k):
    combos = []
    if (k == 1):
        return n 
    for i in range(len(n)): 
        head = n[i:i+1]
        tail = combinations(n[i+1:],k-1)
        for j in range(len(tail)):
            print("tail[j]", tail[j])
            
            combo = head + [tail[j]]
            
            combos.append(combo)
    return combos
result = combinations([1, 2, 3,4], 2)
print(result)