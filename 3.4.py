from collections import defaultdict

def extra_letter(a: str, b: str) -> str:
    count = defaultdict(int)
    

    for char in a:
        count[char] += 1
    

    for char in b:
        if count[char] > 0:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        else:
            return char
    
    return "" 
