#Дан массив, содержащий только 0 и 1. Напишите функцию, которая сортирует его так, чтобы все нули оказались в начале, а все единички - в конце. Решение должно быть in-place.
def sort_binary_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left+=1
        elif arr[right] == 1:
            right -= 1 #если текущий элемент справа равен 1
        else: # если arr[left] == 1 и arr[right] == 0, меняем их местами
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return arr
