def draw_rectangle(n):
    j=0
    
    print("+"+"-" * (n + 2)+"+")
    for i in range(n):
        print('|'+'#'*(n-j), '#' * (j+1)+'|')
        j=j+1
    
    print("+"+"-" * (n + 2)+"+")
draw_rectangle(10)
        
  