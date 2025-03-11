#Дан не отсортированный массив целых чисел. Необходимо перенести в начало массива все четные числа, сохраняя их очередность.
def evenFirst(arr):
    evenIndex = 0
    i=0
    while i<=(len(arr)-1):
        if arr[i] % 2 == 0:
            arr[i], arr[evenIndex] = arr[evenIndex], arr[i]
            evenIndex += 1
        i+=1
    return arr
