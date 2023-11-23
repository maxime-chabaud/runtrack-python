def tri_selection(liste):
    for i in range(len(liste)):
        min_index = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j

        liste[i], liste[min_index] = liste[min_index], liste[i]

L = [7, 11, 42, 39, 2]

tri_selection(L)

print("Liste triée :", L)
