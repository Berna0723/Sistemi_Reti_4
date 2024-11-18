dim = 1000
lista=[]



for i in range (1,dim): #parte da 1 e va fino a max 
    ris=0 
    for num in range (1, i):

        if i %  num ==0 :
            ris= ris + i
            lista.append(i)

    if  ris == i  : 
        print(f" il numero {i} è perfetto")
    else :
        print(f" il numero {i} non è perfetto")

 



