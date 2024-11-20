#scrivere un programma che chieda in input all'utente un nome file di un programma c o python e stampi il numero di righe del file
file = input("Inserisci il nome di un file-> ")
ighe = 0
file = open(file, "r")
lista_righe = file.readlines()
file.close()

for riga in lista_righe:
    numRighe = numRighe + 1
print(f"Le righe del file sono: {numRighe}")