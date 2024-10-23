#fare un ciclo for per contare quante volte appare la letera nella frase

frase = (input("inserisci una frase: "))
lettera = (input("inserisci una lettera: "))
cont = 0

for carattere in frase: 
    if (carattere) == lettera: 
        cont = cont + 1

print(f"la {lettera} è presente {cont} volte")

