def my_long_word(chiffre, phrase):
    mots = phrase.split()
    mots_long = [mot for mot in mots if len(mot) > chiffre]
    return mots_long

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

print("Mots plus longs que le chiffre donné :", resultat)
