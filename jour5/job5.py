def marche(nombre_marche, heigth):
    
    distanceTotal=((((nombre_marche*heigth)*2)*7)/100)
    print("le nombre de marche par semaine :", distanceTotal, "m")
    
marcher=int(input("entrez le nombre de marche:"))
hauteur=int(input("entrez la hauteur des marches:"))

marche(marcher, hauteur)

