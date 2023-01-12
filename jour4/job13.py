liste=[10,20,30,20,10,50,60,40,80,50,40]
resultatlist=[]
for element in liste:
    if element not in resultatlist:
        resultatlist.append(element)
print(resultatlist)