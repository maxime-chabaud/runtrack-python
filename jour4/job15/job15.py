liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

nombres_arrondis = [round(nombre) for nombre in liste_nombres]

nombres_tries = sorted(nombres_arrondis)

print("Liste arrondie et triée dans l'ordre croissant :", nombres_tries)
