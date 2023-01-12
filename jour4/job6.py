liste=[1,2,4,3,6,7,8]
stock=[]
stock=liste[-1]
liste[-1]=liste[0]
liste[0]=stock
print(liste)
