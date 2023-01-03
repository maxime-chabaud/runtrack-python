def calcul(num1,operateur,num2):
    if operateur == "+":
        return num1+num2
    elif operateur == "-":
        return num1-num2
    elif operateur == "%":
        return num1%num2
    elif operateur == "/":
        return num1/num2

print(calcul(1, "+", 6))
print(calcul(1, "-" ,6))
print(calcul(1, "/" ,6))
print(calcul(1, "%" ,6))