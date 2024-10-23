stringa = input("scrivi una frase: ") #input restituisce solo stringhe
#stampare la stringa rimuovendo il primo e ultimo carattere
#len legge il numero di caratteri in una stringa
print(stringa[1:-1])
print(stringa[1: len(stringa)-1])         #si chiama slicing, divido la stringa --> [1:] signofica dal secondo carattere fino alla fine 
#sono uguali                              #[1: -1] stampa da 1 incluso a da destra - 1 non incluso


#stampare gli ultimi 3 caratteri  [da : a]
print(stringa[-3:])

#stampare i primi 3 caratteri
print(stringa[0: 3])

#stampare la stringa rimuovendo il primo e ultimo carattere e tutti i caratteri in posizione pari
print(stringa[1: -1 : 2]) #[inizio(indice iniziale incluso) : fine(indice finale escluso) : salto]

#stampare solo i caratteri in posizione pari
print(stringa[:  : 2])

#stampa la stringa al contrario
print(stringa[: : -1])

