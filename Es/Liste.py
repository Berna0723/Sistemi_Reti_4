lista = ["computer", "casa", "scuola", "python"]
for parola in lista :
    if parola[0] == "c":
        print(f"la parola {parola} inizia con 'c'")


print(lista)

#con le liste valgono le stesse cose delle stringhe slicing
altra_lista= ["lista", "robot"]

lista= lista + altra_lista #concatenazione
print(lista)

lista = lista*3 #concatenazione multipla
print(lista)