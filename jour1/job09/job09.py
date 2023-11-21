nom = "ordinateur"
prix = 250
stock = 20

print(f"""Article: {nom}
    prix : {prix}
    stock : {stock}""")

saisie=int(input("Combien vous en voulez ? "))
print(f"""Article : {nom}
      prix :{prix*1.1}
      stock : {stock-saisie}""")
