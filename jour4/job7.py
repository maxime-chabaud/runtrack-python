L=[8,24,48,2,16]
long=len(L)
multiple3 = 0
for i in range(long):
    if L[i] %3 == 0:
        multiple3=multiple3 +1
print("le nombre de multiple de 3 est de :",multiple3)