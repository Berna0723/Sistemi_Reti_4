#chiedere all'utente un mac address (hex)
#1) fare il controllo che il mac address sia valido 
#2)stamparlo in binario
#3)stampare i primi 3 byte (vendor) del MAC ADDRESS

stringa= input("inserire un MAC ADDRESS")
print(stringa)


lista= stringa.split("-")

for byte in lista : 
    print(byte)
    byte = int(byte,16)
    print(bin(byte))

