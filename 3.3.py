def feed_animals(animals: list[int], food: list[int]) -> int:
    if not animals or not food:
        return 0
    
    animals.sort()
    food.sort()
    
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        
        if count == len(animals):
            break
    
    return count
