def arrondi():

    liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    nouveliste=[]
    for i in liste:
        nombre=round(i)
        nouveliste.append(nombre)
    print(nouveliste)
    result=nouveliste
    for i in range(len(result)):
        for j in range(len(result)):
            if nouveliste[i]>=nouveliste[j] and i<=j:
                nouveliste[i] ,nouveliste[j]=nouveliste[j] , nouveliste[i]
    return nouveliste
arrondi()
   
        
   
        