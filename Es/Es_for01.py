#input frase e lettera e stampare la posizione che la lettera ha nella frase

frase = input("inserisci una frase : ")
carattere = input ("inserisci lettera da cercare :")

for i, valore in enumerate(frase) :
     if (carattere == valore):
        print(f"il carattere si trova in posizione {i}")