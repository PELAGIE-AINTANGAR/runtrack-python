def croissant(l):
    for i in range(len(l)):
        for j in range(len(l)):
              if l[i]>=l[j] and i<=j:
                l[i] ,l[j]=l[j] , l[i]
    return l
A=[8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(croissant(A))