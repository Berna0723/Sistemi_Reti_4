stringa =input("scrivi una frase : ") # input è come il gets del c
#stampa la stringa rimuovendo il primo e l'ultimo carattere

print(stringa[1:-1 ])#per fare lo slicing : estremo sinistro(1) incluso e estremo destro (-1) escluso 

#stampare gli ultimi 3 caratteri 

print(stringa[-3:])
print(stringa[len(stringa)-3:])

"""print(stringa[0:3])
stampare la stringa rimuovendo 
 il primo e ultimo carattere 
e tutti i caratteri in posizione pari
"""

print(stringa[1:-1:2])

#stampare  solo i caratteri in pos pari

print(stringa[::2])

#stampa la stringa al contrario 

print(stringa[::-1])

