n=10
k= ord('a')
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=' ')
        k+=1
    
    print()