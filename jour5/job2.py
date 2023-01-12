def draw_rectangle(width,heigth):
    heigth=heigth-2
    
    print("|","-" * (width - 2),"|") 
    for i in range(heigth):          
        print("|", ' '*(width-2), '|')
        
    print("|","-" * (width - 2),"|")
               
draw_rectangle(10,3)