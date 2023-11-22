def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            return f"Le nombre {nombre} est pair."
        else:
            return f"Le nombre {nombre} est impair."
    else:
        return "Veuillez entrer un nombre entier positif."

# Appels de la fonction avec différentes valeurs
print(verifier_pair_impair(5))
print(verifier_pair_impair(10))
print(verifier_pair_impair(17))
