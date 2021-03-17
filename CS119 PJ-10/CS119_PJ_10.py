#=====================================================================================================
#Author: Manuel Argueta
#Date:11/24/20
#Purpose: The purpose of the following program is to check a Tic-Tac-Toe Game(6 games preset into a 3-dimensonal
#lists) and print out all of the possible winning situations in detail. The program will also allow the user to
#enter a game-board, will store it into a 2-dimensional array, and will then print out all of the winning situations
#in detail.

#START of def winRow1
def winRow1(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    r = 0 #initiates variable r to the value of 0(to check row 1)
    return (t[r][0] == t[r][1] and t[r][1] == t[r][2] and t[r][2] == p) #returns boolean value when the specified condition
#is true or false. The condition returns true when the 1st row is completely full of X's or O's.
#END of def winRow1

#START of def winRow2
def winRow2(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    r = 1 #initiates variable r to the value of 1(to check row 2)
    return (t[r][0] == t[r][1] and t[r][1] == t[r][2] and t[r][2] == p) #returns boolean value when the specified condition
#is true or false. The condition returns true when the 2nd row is completely full of X's or O's.
#END of def winRow2

#START of def winRow3
def winRow3(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    r = 2 #initiates variable r to the value of 2(to check row 3)
    return (t[r][0] == t[r][1] and t[r][1] == t[r][2] and t[r][2] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 3rd row is completely full of X's or O's.
#END of def winRow3

#START of def winCol1
def winCol1(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    c = 0 #initiates variable c to the value of 0(to check column 1)
    return (t[0][c] == t[1][c] and t[1][c] == t[2][c] and t[2][c] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 1st column is completely full of X's or O's.
#END of def winCol1

#START of def winCol2
def winCol2(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    c = 1 #initiates variable c to the value of 1(to check column 2)
    return (t[0][c] == t[1][c] and t[1][c] == t[2][c] and t[2][c] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 2nd column is completely full of X's or O's.
#END of def winCol2

#START of def winCol3
def winCol3(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    c = 2 #initiates variable c to the value of 3(to check column 3)
    return (t[0][c] == t[1][c] and t[1][c] == t[2][c] and t[2][c] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 3rd column is completely full of X's or O's.
#END of def winCol3

#START of def winDiag1
def winDiag1(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    return (t[0][0] == t [1][1] and t[1][1] == t[2][2] and t[2][2] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 1st diagonal is completely full of X's or O's.
#END of def winDiag1

#START of def winDiag2
def winDiag2(t,p): #takes parameters t and p. t is the list and p is the player(either 'X' or 'O')
    return (t[0][2] == t [1][1] and t[1][1] == t[2][0] and t[2][0] == p) #returns boolean value when the specified condition
#is true or fales. The condition returns true when the 2nd diagonal is completely full of X's or O's.
#END of def winDiag2

#START of def show
def show(list): #takes parameter list. list is the list that the function will display on a 3 x 3 format 
   #start of nested for loop to loop through all elements of list
   for i in range(3): #for loop to loop through the 3 rows
       for j in range(3): #for loop to loop through the 3 columns
         print(list[i][j], end = " ") #prints the element at index [i][j] with out printing on a new line
       print(" ") #begins to print on a new line
#END of def show

#START of checkWin
def checkWin(list): #takes parameter list. list is the list that the function will display on a 3 x 3 format 
    winCount = 0 #initiates variable winCount with value 0 to keep traack of the number of winnign situtaions found 
    #in a game board
    if winRow1(list,X) == True: #if statement to check if winRow1 returns True for player X(the first row of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Row 1") #prints out message that notifes user that X has won by row 1
    elif winRow1(list,O) == True: #if statement to check if winRow1 returns True for player O(the first row of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Row 1") #prints out message that notifes user that O has won by row 1
    if winRow2(list,X) == True: #if statement to check if winRow2 returns True for player X(the second row of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Row 2") #prints out message that notifes user that X has won by row 2
    elif winRow2(list,O) == True: #if statement to check if winRow2 returns True for player O(the second row of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Row 2") #prints out message that notifes user that O has won by row 2
    if winRow3(list,X) == True:  #if statement to check if winRow3 returns True for player X(the third row of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Row 3") #prints out message that notifes user that X has won by row 3
    elif winRow3(list,O) == True: #if statement to check if winRow3 returns True for player O(the third row of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Row 3") #prints out message that notifes user that O has won by row 3
    if winCol1(list,X) == True:  #if statement to check if winCol1 returns True for player X(the first column of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Column 1") #prints out message that notifes user that X has won by column 1
    elif winCol1(list,O) == True: #if statement to check if winCol1 returns True for player O(the first column of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Column 1") #prints out message that notifes user that O has won by column 1
    if winCol2(list,X) == True:  #if statement to check if winCol2 returns True for player X(the second column of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Column 2") #prints out message that notifes user that X has won by column 2
    elif winCol2(list,O) == True: #if statement to check if winCol2 returns True for player O(the second column of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Column 2") #prints out message that notifes user that O has won by column 2
    if winCol3(list,X) == True:  #if statement to check if winCol3 returns True for player X(the third column of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Column 3") #prints out message that notifes user that X has won by column 3
    elif winCol3(list,O) == True: #if statement to check if winCol3 returns True for player O(the third column of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Column 3") #prints out message that notifes user that O has won by column 3
    if winDiag1(list,X) == True:  #if statement to check if winDiag1 returns True for player X(the first diagonal of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Diagonal 1") #prints out message that notifes user that X has won by diagonal 1
    elif winDiag1(list,O) == True: #if statement to check if winDiag1 returns True for player O(the first diagonal of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Diagonal 1") #prints out message that notifes user that O has won by diagonal 1
    if winDiag2(list,X) == True:  #if statement to check if winDiag2 returns True for player X(the second diagonal of the gameboard is purely X)
        winCount+=1 #increases winCount by 1
        print("X won by Diagonal 2") #prints out message that notifes user that X has won by diagonal 2
    elif winDiag2(list,O) == True: #if statement to check if winDiag2 returns True for player O(the second diagonal of the gameboard is purely O)
        winCount+=1 #increases winCount by 1
        print("O won by Diagonal 2") #prints out message that notifes user that O has won by diagonal 2
    if winCount == 0: #if statement to check if the winCount == 0 and if true the program will print that gameboard
        #has no winning situations or is a tie
        print("It's a tie!") #prints out message that notifes user that the gameboard is a tie

#start of the defintion of gList which keeps track of the 6 preloaded gameboards
gList = [["none"],#creates empty lists so that the gameboards begin at index 1
    [['O','O','O'], #1st gameboard of gList
     ['O','O','O'],
     ['O','O','O']],
    [['X','X','X'], #2nd gameboard of gList
     ['X','X','X'],
     ['X','X','X']],
    [['X','O','X'], #3rd gameboard of gList
     ['X','X','O'],
     ['X','O','O']],
    [['X','O','O'], #4rd gameboard of gList
     ['O','X','O'],
     ['X','X','O']],
    [['X','O','X'], #5th gameboard of gList
     ['O','X','O'],
     ['X','O','O']],
    [['O','X','O'],#6th gameboard of gList 
     ['X','O','X'],
     ['X','O','X']]
    ]
#end of the defintion of gList which keeps track of the 6 preloaded gameboards

n=1 #initiates variable n with a value of 0 to keep track of line numbers
X = 'X' #initiates variable X that stores the character 'X' 
O = 'O' #initiates variable O that stores the character 'O' 
print("Welcome to the Tic Tac Toe Game Checker by Manuel Argueta!") #prints a welcome message from the user
print(n,"====================================.") #prints a seperation line with the line number
n+=1 #increases the line number by 1
for i in range(1,6+1): #for loop to loop through all 6 of the preset gamebaords
    print("GAME",i," is as follows: ") #prints title with the game number
    show(gList[i]) #calls function show to print the appropraite list
    checkWin(gList[i]) #calls function checkWin to print all of the winning situations(if any)
    print(n,"=====================================.") #prints a seperation line with the line number
    n+=1 #increases the line number by 1

#START of while loop
while True:
    g = [['','',''], #creates empty list g to store the users inputed gameboard
         ['','',''],
         ['','','']]
    s = input("Please enter the game board(enter * to exit): ") #user input to take the users inputed gameboard
    if s == '*': #if statement to check if the user inputed an asterisk
        print(n,"=====================================.")  #prints a seperation line with the line number
        n+=1 #increases the line number by 1
        print("Thank you for playing the Tic Tac Toe Game Checker by Manuel Argueta") #prints a farewell message from 
        #the author
        print(n,"=====================================.") #prints a seperation line with the line number
        break #breaks the while loop and the program
    d = 0 #initiates variable d with value 0 to keep track of the 9 charcters inputed by the user
    #start of nested for loop to loop through all elements of empty list g
    for i in range(3): #for loop to loop through the 3 rows
        for j in range(3): #for loop to loop through the 3 columns
            g[i][j] = s[d] #assignment statmeant to slot the corresponding element of the users input into the 
            #the correct position of list g
            d+=1 #increases d by 1 to slot the next character of the users input
    show(g) #calls function show to print list g in 3 x 3 format
    checkWin(g) #calls function checkWin to print all winning situations of the users inputed gamebaord
    print(n,"=====================================.") #prints a seperation line with the line number
    n+=1 #increases the line number by 1
