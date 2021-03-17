#=======================================================================================
#Author: Manuel Argueta
#Date: 10/01/2020
#Purpose: The following program creates a game where the user and a dealer roll a dice to either win/lose money. The user 
#inputs the bet amount each round and the game continues until the user inputs 0 as the bet anount.

#MAIN Program=======================================
import random #import libraries neccesary to use the random function
n = 1 # declares variable n to keep track of line numbers
print("Welcome to the Rolling Dice Game by Manuel Argueta!")
print(n,"=============================================.") # prints line seperator and line number
n+=1 #increases line count by one
userMoney = 100 # declares variable userMoney to track of the users earnings throughout the game
print("You have $"+str(userMoney)+ " dollars to start!") #prints the amount of money the user has initially
print(n,"=============================================.") # prints line seperator and line number
n+=1 #increases line count by one
#start of the while loop
while True: 
    betAmount = int(input("Please enter your bet (enter 0 to quit): ")) #prompts the user to enter bet 
    if betAmount == 0: #if statement to check if the bet entered is 0
        print(n,"=============================================.") # prints line seperator and line number
        n+=1 #increases line count by one
        print("Thank you for playing the Rolling Dice Game by Manuel Argueta") #thank you message to user
        print(n,"=============================================.") # prints line seperator and line number
        x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit: ") #gives user exit instructions
        break #breaks/ends the while loop if the bet amount is 0
    userRoll = random.randint(1,6) #simulates the rolling of dice using random()
    dealerRoll = random.randint(1,6) #simulates the rolling of dice using random()
    print("You rolled a " +str(userRoll)+". The dealer rolled "+str(dealerRoll)+".") #prints the users and delaers roll(1-6)
    if userRoll == dealerRoll: #if statement to check if the rolls are equal
        print("It's a tie! You still have $"+ str(userMoney) +" dollars") #prints a tie message and the users current money
    elif userRoll > dealerRoll: #else if statement to check if the users roll is larger than the dealers roll
        userMoney += betAmount #adds the bet amount to the user total money
        print("You won! You now have $"+ str(userMoney) +" dollars!") #prints a winning message and updated money
    elif dealerRoll > userRoll: #else if statement to checl if the dealers roll is larger than the users roll
        userMoney -= betAmount #subtracts the bet amount from the users money
        print("You lost! You now have $"+ str(userMoney) +" dollars.") #prints loss message and the users updated money
    print(n,"=============================================.")  # prints line seperator and line number
    n+=1 #increases line count by one
#end of the while loop

#END of MAIN program==========================================
    
