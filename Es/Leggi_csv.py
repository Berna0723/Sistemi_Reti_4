#scrivere un programma in pyton che legga un file csv e carichi ogni colonna una lista saltando l'intestazione
file= open("file.csv", "r")

lista_righe= file.readlines()



for riga in lista_righe:
    if(riga== 0 ):
        

    lista_parole = riga.split(" ")# spezzza la stringa sul carattere passato come parametro
    print(lista_parole)