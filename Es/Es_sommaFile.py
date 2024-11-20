file = open("./dati.txt", "r")
righe_file = file.readlines()  # Restituisce la lista delle righe del file
file.close()



for indice, riga in enumerate(righe_file):
    print(riga[:-1])  # Stampa la riga senza il carattere di newline
    valori_riga = riga.split(" ")  # Spezza la stringa sul carattere passato come parametro
    # print(valori_riga)
    somma_valori = 0
    valore_minimo = 0
    valore_massimo = 0
    contatore_valori = 0

    for valore in valori_riga:
        if valore_minimo == 0:
            valore_minimo = valore
        elif valore < valore_minimo:
            valore_minimo = valore

        if valore_massimo == 0:
            valore_massimo = valore
        elif valore > valore_massimo:
            valore_massimo = valore

        somma_valori += int(valore)
        contatore_valori += 1
        media_valori = somma_valori / contatore_valori

    print(f"Somma riga numero {indice}: {somma_valori}, il minimo è: {valore_minimo}, il massimo: {valore_massimo}, e la media è: {media_valori}")

