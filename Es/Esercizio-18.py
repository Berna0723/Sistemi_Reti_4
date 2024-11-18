num1 = int(input("Inserire un numero -> "))
num2 = int(input("Inserire un numero -> "))

lista_numeri = [0 , 0 , 0 , 0]

somma_Quadrati = (num1 * num1) + (num2 * num2)

quadrato_Somma = (num1 + num2) * (num1 + num2)

differenza_Quadrato = (num1 * num1) - (num2 * num2)

quadrato_Differenza = (num1 - num2) * (num1 - num2)

for i, valore in enumerate(lista_numeri):
    if(i == 0):
        valore = somma_Quadrati
        print(valore)
    if(i == 1):
        valore = quadrato_Somma
        print(valore)
    if(i == 2):
        valore = differenza_Quadrato
        print(valore)
    if(i == 3):
        valore = quadrato_Differenza
        print(valore)