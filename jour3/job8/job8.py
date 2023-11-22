def miam (type,saison):
    if type==("fruits"):
        if saison== ("hiver"):
            return ("orange,mandarine,kiwi")
        elif saison== ("ete"):
            return ("poire,fraise,cassis")
    if type==("legume"):
        if saison== ("hiver"):
            return ("carotte,endive,topinambour")
        elif saison== ("ete"):
            return ("aubergine,navet,artichaut")

print(miam("fruits","hiver"))
print(miam("fruits","ete"))
print(miam("legume","hiver"))
print(miam("legume","ete"))