def max_min_multiplication(data):
    if len(data) < 3:
        return -1
    
    min_index = 1
    i = 1
    while 2 * i + 1 < len(data):
        i = 2 * i + 1
        min_index = i
    

    max_index = 2
    i = 2
    while 2 * i + 2 < len(data):
        i = 2 * i + 2
        max_index = i
    
    if min_index >= len(data) or max_index >= len(data):
        return -1
    
    return data[min_index] * data[max_index]
