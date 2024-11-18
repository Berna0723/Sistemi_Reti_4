def stringaLunga(lista):
    parola = lista[0]
    for valore in lista:
        if(len(valore) > len(parola)):
            parola = valore
    return parola

lista = ["Casa", "Fiore", "Stella"]
print(f"la stringa più lunga è {stringaLunga(lista)}")