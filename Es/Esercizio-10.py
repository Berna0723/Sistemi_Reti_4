lista_voti = [4 , 8 , 6 , 5 , 7 , 9 , 10]

for i in range (1, len(lista_voti) - 1): 
    print(lista_voti[i])

#2° punto:
for i, valore in enumerate(lista_voti): 
    if(i == 3): 
        valore = 10
    print(f" Nella cella {i} trovo il valore {valore}")

#3° punto:
for i in range (0, len(lista_voti)): 
    if(i <= 2):
        print(lista_voti[i])


