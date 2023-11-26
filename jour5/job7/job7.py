def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_sup = ((note // 5) + 1) * 5
            if multiple_de_5_sup - note < 3:
                notes_arrondies.append(multiple_de_5_sup)
            else:
                notes_arrondies.append(note)

    return notes_arrondies


liste_notes = [37, 45, 82, 91, 64]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes initiales :", liste_notes)
print("Notes arrondies :", notes_arrondies)
