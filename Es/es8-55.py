stringa = input("Inserisci una parola di almeno 8 lettere: ")
if len(stringa) >= 8:
    print(stringa[:2]+ "?" + stringa[3:])
else:
    print("La parola deve avere almeno 8 lettere.")
