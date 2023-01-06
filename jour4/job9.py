L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

max = L[0]
min = L[0]

for nombre in L:
    if nombre > max:
        max = nombre
    if nombre < min:
        min = nombre

print("Le nombre maximum est", max)
print("Le nombre minimum est", min)