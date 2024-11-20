def controllo(lista_mac): #controlla se la lista ha lunghezza giusta come il mac address
    if(len(lista_mac) != 6):
        return False
    else:
        return True

def controlloNome(lista): #controlla che il nome contenga caratteri presenti nel mac address, se ne trova uno diverso esce
    mac = input("inserisci mac address: ")
    for lettera in mac:
        if lettera not in lista:
            exit()
            
    return mac
        
    

lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "-"]


mac = controlloNome(lista)

lista_mac = mac.split("-")

if(controllo(lista_mac)): #converte prima da esa e dec, poi da dec in binario
    for valore in lista_mac:
        num = int(valore, 16)
        num = bin(num)
        print(num)
else:
    print("errore")
