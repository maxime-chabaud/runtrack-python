def distance_toilettes_par_semaine(nb_marches, hauteur_marche):
    nb_jours_semaine = 7
    nb_allers_retours_jour = 2
    distance_totale_cm = nb_marches * hauteur_marche * nb_allers_retours_jour * nb_jours_semaine
    distance_totale_m = distance_totale_cm / 100

    return distance_totale_m

nb_marches = 100
hauteur_marche = 20
distance_totale = distance_toilettes_par_semaine(nb_marches, hauteur_marche)
print(f"Pour {nb_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
