#Дано два отсортированных массива. Необходимо написать функцию которая объединит эти два массива в один отсортированный.
def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0; j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array
