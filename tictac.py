tictac = ["0","0","0","0","0","0","0","0","0"]

def tictactoe():
    print(tictac[0],tictac[1],tictac[2])
    print(tictac[3],tictac[4],tictac[5])
    print(tictac[6],tictac[7],tictac[8])
tictactoe()

print("""
topleft, topmiddle, topright
left, middle, right
bottomleft, bottommiddle, bottomright
""")

for c in range(5):
    x  = input("where do you want to place(x): ")
    
    if x == "topright":
        tictac[2]= "x"
        tictactoe()
    
    elif x == "topleft":
        tictac[0]= "x"
        tictactoe()

    elif x == "topmiddle":
        tictac[1]= "x"
        tictactoe()

    elif x == "left":
        tictac[3]= "x"
        tictactoe()
    
    elif x == "middle":
        tictac[4]= "x"
        tictactoe()

    elif x == "right":
        tictac[5]= "x"
        tictactoe()
    
    elif x == "bottomleft":
        tictac[6]= "x"
        tictactoe()
    
    elif x == "bottommiddle":
        tictac[7]= "x"
        tictactoe()
    
    elif x == "bottomright":
        tictac[8]= "x"
        tictactoe()


    y  = input("where do you want to place(y): ")
    
    
    if y == "topright":
        tictac[2]= "y"
        tictactoe()
    
    elif y == "topleft":
        tictac[0]= "y"
        tictactoe()

    elif y == "topmiddle":
        tictac[1]= "y"
        tictactoe()

    elif y == "left":
        tictac[3]= "y"
        tictactoe()
    
    elif y == "middle":
        tictac[4]= "y"
        tictactoe()

    elif y == "right":
        tictac[5]= "y"
        tictactoe()
    
    elif y == "bottomleft":
        tictac[6]= "y"
        tictactoe()
    
    elif y == "bottommiddle":
        tictac[7]= "y" 
        tictactoe()
    
    elif y == "bottomright":
        tictac[8]= "y"
        tictactoe()

  
if x in tictac[0] and tictac[4] and tictac[8]:
    print("you won")