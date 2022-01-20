tictac = ["0","0","0","0","0","0","0","0","0"]

print(tictac[0],tictac[1],tictac[2])
print(tictac[3],tictac[4],tictac[5])
print(tictac[6],tictac[7],tictac[8])

for x in range(9):
    x  = input("where do you want to place(x): ")
    

    if x == "topright":
        tictac[2]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif x == "topleft":
        tictac[0]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif x == "topmiddle":
        tictac[1]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif x == "left":
        tictac[3]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif x == "middle":
        tictac[4]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif x == "right":
        tictac[5]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif x == "bottomleft":
        tictac[6]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif x == "bottommiddle":
        tictac[7]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif x == "bottomright":
        tictac[8]= "x"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    y  = input("where do you want to place(y): ")
    
    
    if y == "topright":
        tictac[2]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif y == "topleft":
        tictac[0]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif y == "topmiddle":
        tictac[1]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif y == "left":
        tictac[3]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif y == "middle":
        tictac[4]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])

    elif y == "right":
        tictac[5]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif y == "bottomleft":
        tictac[6]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif y == "bottommiddle":
        tictac[7]= "y" 
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])
    
    elif y == "bottomright":
        tictac[8]= "y"
        print(tictac[0],tictac[1],tictac[2])
        print(tictac[3],tictac[4],tictac[5])
        print(tictac[6],tictac[7],tictac[8])