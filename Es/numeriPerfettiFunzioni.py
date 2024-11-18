dim = 1000
lista=[]
#documentazione di una funzione 
"""la funzione calcola la somma dei divisori di un numero .
Parametri : numero(int)
Restituisce : somma divisori(int)

"""
def sommaDivisori(numero): 
    sommaDiv= 0 
    for num in range(1, numero):
        if( numero % num ==0) :
            sommaDiv = sommaDiv +num
    return sommaDiv

for i in range (1,dim): #parte da 1 e va fino a max 
    sommaDiv= sommaDivisori(i)
    if(sommaDiv== i):
        print(f"il numero {i} è un numero perfetto")
 
 #in python si possono ritornare un sacco di variabili 

 