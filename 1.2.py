#Дан массив целых чисел. Необходимо повернуть (сдвинуть) справа налево часть массива, которая указана вторым параметром.Сделать это надо за линейное время без дополнительных аллокаций
def reverseArray(arr, left, right):
    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1


def solution(arr, k):
    n = len(arr)
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, k%n - 1)
    reverseArray(arr, k%n, n - 1)
    return arr
