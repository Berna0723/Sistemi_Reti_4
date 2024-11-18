# Lista delle vocali
vocali = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Chiedere all'utente di inserire un testo
testo = input("Inserisci un testo: ")

# Utilizzare una list comprehension per creare una lista di caratteri senza vocali
testo_senza_vocali=''

testo_senza_vocali = [lettera for lettera   in testo if lettera not in vocali]

# Stampare il testo senza vocali
print(f"Testo senza vocali: {testo_senza_vocali}")

parolasenzavoc='CIAO'.join(testo_senza_vocali)# join prende come parametro una lista di stringhe e le concatena usando il carattere fornito
                                          #in questo caso la stringa vuota 
print(f"parola senza vocali : {parolasenzavoc}")
