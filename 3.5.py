def two_sum(data: list[int], target: int) -> list[int]:
    cache = {}
    
    for i, num in enumerate(data):
        cache[num] = i
    

    for i, num in enumerate(data):
        diff = target - num
        if diff in cache and cache[diff] != i:  
            return [i, cache[diff]]
    
    return [] 
