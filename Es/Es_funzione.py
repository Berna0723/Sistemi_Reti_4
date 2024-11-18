def operazioniNum (num1  num2):
    risP= num1 * num2
    risS=num1 +num2
    risD=num1 / num2
    risM=num1 - num2

    return risD , risM, risP, risS





num1= input("inserire un numero :")
num2= input("inserire secondo numero :")

div,meno,per,add= operazioniNum(num1, num2)

print(f"somma: {add}, sottrazzione : {meno}, moltiplicazione {per}, divisione: {div}")

