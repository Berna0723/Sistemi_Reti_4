# una lista che contenga tutti i quadreati perfetti de numeri da 1 a 10ma solo quando sono dispari 

quadrati = [i **2 for  i in range (1,10) if i **2 % 2 != 0]

print(quadrati)