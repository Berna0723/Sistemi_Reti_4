""" creare la lista che contiene le lunghezze 
delle parole presenti nella lista parole """

parole=["ciao", "scuola", "casa"]
lunghezze = [len(p) for p in parole]
print(lunghezze)

#creare la lista che contiene solo il num di lettere delle parole che iniziano con c
parole=["ciao", "scuola", "casa"]
lunghezze = [len(p) for p in parole if p[0]=="c"]
print(lunghezze)
