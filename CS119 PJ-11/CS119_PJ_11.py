#==============================================================================================
#Author: Manuel Argueta
#Date: 12/09/2020
#Purpose: The following program will take 4 preloaded 9 x 9 sudoku game boards and print out eveything "wrong"
#and "correct" with the gameborad. It will check the board row by row, column by column, and square by square 
#and tell the user what needs to be fixed.

#START of def show
def show(list): #takes parameter list. list is the list that the function will display on a 9 x 9 format 
   #start of nested for loop to loop through all elements of list
   for i in range(9): #for loop to loop through the 9 rows
       for j in range(9): #for loop to loop through the 9 columns
         print(list[i][j], end = " ") #prints the number at index [i][j] with out printing on a new line
       print(" ") #begins to print on a new line
#END of def show

#START of def rowCheck 
def rowCheck(g,row): #takes parameters g and row. g is the 2d list and row is the row that the function will check
    correctList = [1,2,3,4,5,6,7,8,9] #initiaites and declares list correctList with the numbers 1 through 9
    #with no repetitions
    sList = g[row] #assigns newly initiated sList the 9 values of the row the fucntion is checking(parameter row)
    cList = [] #creates a empty list called cList
    #for loop to transfer the elements of sList to cList
    for i in sList:
        cList.append(i) #appends the element of sList at index i to cList
    cList.sort() #sorts the numbers in cList from least to greatest
    return (cList == correctList) #returns True when cList is equal to correctList(basically it means the row is okay)
#END of def rowCheck

#START of def colCheck 
def colCheck(g,col): #takes parameters g and col. g is the 2d list and col is the column that the function will check
    correctList = [1,2,3,4,5,6,7,8,9] #initiaites and declares list correctList with the numbers 1 through 9
    #with no repetitions
    sList = [] #creates a empty list called sList
    cList = [] #creates a empty list called cList
    #for loop that loops nine times to give sList the 9 numbers of the specified column(parameter col)
    for i in range(9):
        sList.append(g[i][col]) #appends the element(number) at the position g[i][col] which makes the list equal
        #to the specified column(col)
    #for loop to transfer the elements of sList to cList
    for j in sList:
        cList.append(j) #appends the element of sList at index j to cList
    cList.sort()  #sorts the numbers in cList from least to greatest
    return (cList == correctList) #returns True when cList is equal to correctList(basically it means the column is okay)
#END of def colCheck

#START of def squareCheck 
def squareCheck(g,squ): #takes parameters g and squ. g is the 2d list and squ is the square that the function will check
    correctList = [1,2,3,4,5,6,7,8,9] #initiaites and declares list correctList with the numbers 1 through 9
    #with no repetitions
    #defines sList1 to get all the numbers found in the gameboards first sqaure(3x3 area)
    sList1=[g[0][0],g[0][1],g[0][2],g[1][0],g[1][1],g[1][2],g[2][0],g[2][1],g[2][2]]  
    #defines sList2 to get all the numbers found in the gameboards second sqaure(3x3 area)
    sList2=[g[0][3],g[0][4],g[0][5],g[1][3],g[1][4],g[1][5],g[2][3],g[2][4],g[2][5]]  
    #defines sList3 to get all the numbers found in the gameboards third sqaure(3x3 area)
    sList3=[g[0][6],g[0][7],g[0][8],g[1][6],g[1][7],g[1][8],g[2][6],g[2][7],g[2][8]]  
    #defines sList4 to get all the numbers found in the gameboards fourth sqaure(3x3 area)
    sList4=[g[3][0],g[3][1],g[3][2],g[4][0],g[4][1],g[4][2],g[5][0],g[5][1],g[5][2]]  
    #defines sList5 to get all the numbers found in the gameboards fifth sqaure(3x3 area)
    sList5=[g[3][3],g[3][4],g[3][5],g[4][3],g[4][4],g[4][5],g[5][3],g[5][4],g[5][5]]  
    #defines sList6 to get all the numbers found in the gameboards sixth sqaure(3x3 area)
    sList6=[g[3][6],g[3][7],g[3][8],g[4][6],g[4][7],g[4][8],g[5][6],g[5][7],g[5][8]]  
    #defines sList7 to get all the numbers found in the gameboards seventh sqaure(3x3 area)
    sList7=[g[6][0],g[6][1],g[6][2],g[7][0],g[7][1],g[7][2],g[8][0],g[8][1],g[8][2]]  
    #defines sList8 to get all the numbers found in the gameboards eigth sqaure(3x3 area)
    sList8=[g[6][3],g[6][4],g[6][5],g[7][3],g[7][4],g[7][5],g[8][3],g[8][4],g[8][5]]  
    #defines sList9 to get all the numbers found in the gameboards ninth sqaure(3x3 area)
    sList9=[g[6][6],g[6][7],g[6][8],g[7][6],g[7][7],g[7][8],g[8][6],g[8][7],g[8][8]] 
    sList = [sList1,sList2,sList3,sList4,sList5,sList6,sList7,sList8,sList9] #creates a list called sList
    #thats stores all 9 lists from sList1 - sList9  
    cList = [] #creates a empty list called cList
    #for loop to transfer the elements of the list found at sList[squ] to cList
    for i in sList[squ]: 
        cList.append(i) #appends the element of sList at index i to cList
    cList.sort() #sorts the numbers in cList from least to greatest
    return (cList == correctList)  #returns True when cList is equal to correctList(basically it means the column is okay)
#END of def squareCheck

#START of def checkGame
def checkGame(g): 
    errorCount = 0 #initiates variable errorCount to count how many times an error is found in the gameboard
    #for loop to check all 9 of the gameboards rows
    for r in range(9):
         if rowCheck(g,r) == False: #if statement to check if there is an error in row r
             print("Row " + str(r+1)+ " has a problem.") #prints a message letting the user know that there is an error in 
             #row r
             errorCount +=1 #increases error count by 1
    #for loop to check all 9 of the gameboards columns
    for c in range(9):
         if colCheck(g,c) == False: #if statement to check if there is an error in column c
             print("Column " + str(c+1)+ " has a problem.") #prints a message letting the user know that there is an error in 
             #column c
             errorCount +=1 #increases error count by 1
    #for loop to check all 9 of the gameboards squares
    for s in range(9):
         if squareCheck(g,s) == False: #if statement to check if there is an error in square s
             print("Square " + str(s+1)+ " has a problem.") #prints a message letting the user know that there is an error in 
             #square s
             errorCount +=1 #increases error count by 1
    if errorCount == 0: #if statement to check if there were 0 errors in the sudoku gameboard
        print("Congratulations! You won the game!") #prints a message to the user letting them know that the gameboard is perfect
#END of def checkGame

#MAIN PROGRAM==================================================================================
#definition of Game 1
#col:  0 1 2 3 4 5 6 7 8  #row: 
g1 = [[1,2,3,4,5,6,7,8,9],# 0
      [2,3,4,5,6,7,8,9,1],# 1
      [3,4,5,6,7,8,9,1,2],# 2
      [4,5,6,7,8,9,1,2,3],# 3
      [5,6,7,8,9,1,2,3,4],# 4
      [6,7,8,9,1,2,3,4,5],# 5
      [7,8,9,1,2,3,4,5,6],# 6
      [8,9,1,2,3,4,5,6,7],# 7
      [9,1,2,3,4,5,6,7,8]]# 8
#definiton of Game 2
#col:  0 1 2 3 4 5 6 7 8  #row:
g2 = [[1,2,3,4,5,6,7,8,9],# 0
      [4,5,6,7,8,9,1,2,3],# 1
      [7,8,9,1,2,3,4,5,6],# 2
      [2,3,4,5,6,7,8,9,1],# 3
      [5,6,7,8,9,1,2,3,4],# 4
      [8,9,1,2,3,4,5,6,7],# 5
      [3,4,5,6,7,8,9,1,2],# 6
      [6,7,8,9,1,2,3,4,5],# 7
      [9,1,2,3,4,5,6,7,8]]# 8
#definition of Game 3
#col:  0 1 2 3 4 5 6 7 8  #row
g3 = [[1,2,3,4,5,6,7,8,2],# 0
      [4,5,6,7,8,9,1,2,3],# 1
      [7,8,9,1,2,3,4,5,6],# 2
      [2,3,4,5,6,7,8,9,1],# 3
      [5,6,7,8,9,1,2,3,4],# 4
      [8,9,1,2,3,4,5,6,7],# 5
      [3,4,5,6,7,8,9,1,2],# 6
      [6,7,8,9,1,2,3,4,5],# 7
      [9,1,2,3,4,5,6,7,8]]# 8
#definition of Game 4
#col:  0 1 2 3 4 5 6 7 8  #row
g4 = [[1,2,3,4,5,6,7,8,9],# 0
      [4,5,6,7,8,9,1,2,3],# 1
      [7,8,9,1,2,3,4,5,6],# 2
      [2,3,4,5,6,7,8,9,1],# 3
      [5,6,7,8,9,1,2,3,4],# 4
      [8,9,1,2,3,4,5,6,7],# 5
      [3,4,5,6,7,8,9,1,2],# 6
      [6,7,8,9,1,8,3,4,5],# 7
      [9,1,2,3,4,5,6,7,8]]# 8

gameList = [g1,g2,g3,g4] #defines list gameList to stores gameboards g1 -g4
n = 1 #initiates variable n to keep track of line numbers
print("Welcome to the Sudoku Game Checker by Manuel Argueta!") #prints a welcome message from the author
for i in range(1,4+1): #for loop to loop through all of the gameboards g1-g4
    print(n,"===================================.") #prints a line number and a seperation line
    n+=1 #increases line number by 1
    if i == 4: #if statement to check if the for loop is on the 4th and final iteration
        print("Your Game " + str(i) + " is as follows: ") #prints title to let the user know what game is being checked
        show(gameList[i-1]) #calls function show to print out the current gameboard in a 9 x 9 format
        print("Your Game " + str(i) + ": ") #prints a header to let the user know the result is going to be printed
        checkGame(gameList[i-1]) #calls function checkGame to check if there is anything wrong with the gameboards and print anything that 
        #is wrong with them and a congrats message if not
        print(n,"===================================.")  #prints a line number and a seperation line
        n+=1 #increases line number by 1
        print("Thank you for using this Sudoku Game Checker by Manuel Argueta!") #prints a farewell message from the author
        print(n,"===================================.")  #prints a line number and a seperation line
        break #breaks the loop and ends the program
    print("Your Game " + str(i) + " is as follows: ") #prints title to let the user know what game is being checked
    show(gameList[i-1]) #calls function show to print out the current gameboard in a 9 x 9 format
    print("Your Game " + str(i) + ": ") #prints a header to let the user know the result is going to be printed
    checkGame(gameList[i-1]) #calls function checkGame to check if there is anything wrong with the gameboards and print anything that 
    #is wrong with them and a congrats message if not
