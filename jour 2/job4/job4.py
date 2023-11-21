# Fonction pour vérifier si l'entrée est un entier supérieur à zéro
def verifier_entier_positif():
    while True:
        try:
            valeur = int(input("Entrez un entier supérieur à zéro : "))
            if valeur > 0:
                return valeur
            else:
                print("Veuillez entrer un entier supérieur à zéro.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Demander à l'utilisateur de saisir un entier supérieur à zéro
N = verifier_entier_positif()

# Afficher les tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"Table de multiplication de {i}:")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")
    print()  # Ajouter une ligne vide pour séparer les tables
