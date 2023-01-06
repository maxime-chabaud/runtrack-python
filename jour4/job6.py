def inverse():
    L = list(range(1, 11))
    L[0],L[-1] = L[-1], L[0]
    return L
print(inverse())