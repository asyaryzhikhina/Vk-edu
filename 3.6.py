def shell_sort(arr):
    n = len(arr)
    gap = n // 2  
    
    while gap > 0:

        for current_position in range(gap, n):
  
            temp = arr[current_position]
  
            inner_position = current_position
            while inner_position >= gap and arr[inner_position - gap] > temp:
                arr[inner_position] = arr[inner_position - gap]
                inner_position -= gap

            arr[inner_position] = temp
        gap = gap // 2  
    
    return arr
