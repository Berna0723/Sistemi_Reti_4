import random

alice = random.randint(1, 6)

bob = random.randint(1, 6)

print(alice, bob)

if(alice > bob):
    print(f"la vincitrice è alice con il risultato di: {alice}")
elif(alice == bob):
    print(f"i concorrenti hanno lo stesso risultato")
else:
    print(f"il vincitore è bob con il risultato di: {bob}")