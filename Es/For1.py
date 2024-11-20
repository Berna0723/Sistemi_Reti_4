#il ciclo for in python usa quasi sempre stringhe o liste 

numeri= [ 3.1, -4, 2 ,"ciao", "a", print]

#ciclo for sulla lista  Pythonico 

for valore in numeri : 
    print(valore)

#ciclo for sulla lista C-style 
for i in range(0, len(numeri)): #len(numeri) prende la lunghezza della stringa 
    print(numeri[i])

#ciclo for sulla lista per indice e per valore Pythonico

for i,valore in enumerate(numeri): # enumerate ti da sia l'indice che il valore delle varie celle dell'indice  
    print(f"Nella cella {i} trovo : {valore} ")

    