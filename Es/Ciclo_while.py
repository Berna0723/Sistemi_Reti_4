num =-1
while num<0 :
    num =int (input("inserisci un numero maggiore o uguale a 0 ->"))
print(f"il numero è {num}")

#while true in ambito informatico è sbagliato ma in ambito robotico no 

while true :
    num=int (input("inserisci un numero maggiore o uguale a 0 ->"))
    if num >=0:
        break
print(f"il numero è {num}")