def binary_search_sqrt(target: int) -> int:
    if target < 0:
        raise ValueError("Target must be a non-negative integer")
    
    left, right = 0, target
    
    while left <= right:
        middle = (left + right) // 2
        middle_squared = middle * middle
        
        if middle_squared > target:
            right = middle - 1
        elif middle_squared < target:
            left = middle + 1
        else:
            return middle
    
    return right
