dim = 200
cont = 0
for i in range (1,dim): #parte da 1 e va fino a max 
    if((i**.5) % 1  == 0):#.5 equivale  0,5, i ** eleva alla potenza 
        print(f" {i} è un quadrato perfetto {cont}")
        cont+=1

print(f"i quadrati perfetti minori di {dim} sono {cont}")
