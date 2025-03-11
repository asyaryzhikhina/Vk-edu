#Задача: есть массив с оценками, среди которых есть 0. Необходимо все оценки, равные нулю перенести в конец массива
def zeroend(arr):
    Index = 0
    i=0
    while i<=len(arr)-1:
        if arr[i] == 0:
            Index += 1
        else:
            arr[i], arr[i-Index]=arr[i-Index], arr[i]
        i+=1
    return arr
