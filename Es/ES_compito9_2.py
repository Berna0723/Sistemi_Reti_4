#inserire una letterea dell'alfabeto da tastiera e detreminare se è una vocale o una consonante 
lettera = (input("inserisci una lettera: ")).lower
vocali=["a","e","i","o","u"]
if lettera in vocali  :
    print(f"{lettera} è una vocale ") 
 
else : 
    print(f"{lettera} è una consonante")
