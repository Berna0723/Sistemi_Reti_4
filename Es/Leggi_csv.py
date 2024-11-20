#1 scivere un programma che legga il file csv e carichi ogni colonna in una lista
#2 (CALCOLA RIGHE)scrivere un programma che CHIEDA IN INPUT ALL'UTENTE UN NOME FILE DI UN PROGRAMMA C/PYTHINE E STAMPI IL NUMERO DI RIGHE DI UN FILE

file= open("./file.csv", "r")
lista_righe = file.readlines()#restituisce la lista delle righe del file
file.close()

for i,riga in enumerate(lista_righe):
    if (i != 0):
        print(riga)
    #lista_righe = riga.split(" ")#spezza la stringa sul carattere passato come parametro 
    #print(lista_righe)