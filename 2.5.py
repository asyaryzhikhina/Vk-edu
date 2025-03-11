def is_subsequence(a, b):
    pointer_a = 0
    for char_b in b:
        if pointer_a < len(a) and a[pointer_a] == char_b:
            pointer_a += 1
    return pointer_a == len(a)
