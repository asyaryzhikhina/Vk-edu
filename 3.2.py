import math

def copy_time(n: int, x: int, y: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return min(x, y)
    
    left = 0
    right = (n - 1) * max(x, y)
    
    while left + 1 < right:
        mid = (left + right) // 2
        copies = (mid // x) + (mid // y)
        
        if copies < n - 1:
            left = mid
        else:
            right = mid
    
    return right + min(x, y)
