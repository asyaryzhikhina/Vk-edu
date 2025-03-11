def is_subsequence(a, b):
    i = 0  
    len_a = len(a)
    len_b = len(b)

    for el2 in range(len_b):
        if i < len_a and a[i] == b[el2]:
            i += 1

    return i == len_a
