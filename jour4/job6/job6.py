def echanger_premiere_derniere(liste):
    if liste:  # Vérifie si la liste n'est pas vide
        premiere_valeur = liste[0]
        derniere_valeur = liste[-1]
        liste[0] = derniere_valeur
        liste[-1] = premiere_valeur
        return liste
    else:
        return "La liste est vide."

# Exemple d'une liste non vide
ma_liste = [1, 2, 3, 4, 5]

# Affichage de la liste avant l'échange
print("Avant l'échange :", ma_liste)

# Échange des valeurs de la première et de la dernière case
ma_liste = echanger_premiere_derniere(ma_liste)
print("Après l'échange :", ma_liste)
