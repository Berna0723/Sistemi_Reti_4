file= open("./File.txt", "r")
lista_righe= file.readlines() #restituisce la lista delle righe del file
file.close()
for riga in lista_righe:
    lista_parole = riga.split(" ")# spezzza la stringa sul carattere passato come parametro
    print(lista_parole)
    



