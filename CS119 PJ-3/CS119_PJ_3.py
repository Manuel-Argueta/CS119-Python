#-------------------------------------------------------------------------------------------------.
#Author: Manuel Argueta
#Date: 09/30/20
#Purpose: The following program creates a game where the user and a dealer roll 2 dice and win/lose money.
#MAIN Program: ======================================================================================
import random #imports libraries neccesary to use the random function
n=1 #creates variable n which keeps track of line seperator numbers
print("Welcome to the Rolling 2 Dice Game by Manuel Argueta!") #introduces the name of the game and the author to the user
print(n,"============================================================.") #prints seperation line
n+=1 #increases the line count by 1
userMoney = 100 #defines variable userMoney with value of 100; stores the amount of money the user has
dealerMoney = 100 #defines variable dealerMoney with value of 100; stores the amount of money the dealer has
print("You have $"+ str(userMoney) + " dollars to start. The dealer also has $" + str(dealerMoney) +" dollars to start.") #prints
#the amount of money the user and dealer have at the start of the game
betAmount = int(input("Enter the bet you would like to place(enter 0 to quit): ")) #gets the amount that the user will bet each time
#the dice is rolled
if betAmount == 0: #if statement to check if the bet inputed by user is 0
    exit() #exits the console if the bet is 0
print(n,"============================================================.") #prints seperation line
n+=1 #increases the line count by 1
while True: #creates a while loop that will continue until a condition is false
    userRoll = (random.randint(1,6) + random.randint(1,6)) #uses the random function to simulate the rolling of two dice and adding
    # the rolled values together as the users roll
    dealerRoll = (random.randint(1,6) + random.randint(1,6)) #uses the random function to simulate the rolling of two dice and adding
    # the rolled values together as the dealers roll
    print("You rolled "+ str(userRoll)+". The dealer rolled "+ str(dealerRoll) + ".") #prints both the users roll and the dealers roll
    if userRoll == dealerRoll: #checks if the dealers and users roll are equal
        print("Its a tie! No one loses or earns money!") #prints a message letting the user know that a tie has occured 
        print(n,"============================================================.") #prints seperation line
        n+=1                                                                     #increases the line count by 1
    elif userRoll > dealerRoll: #else if statment to check if the users roll is larger than the dealers roll
        userMoney += betAmount #adds the bet amount to the users money
        dealerMoney-= betAmount #subtracts the ebt amount from the dealers money
        print("You won! You now have $"+str(userMoney)+" dollars. The dealer has $"+ str(dealerMoney)+" dollars.") #prints a message that lets
        # the user know that they have won money and displays both the users and dealers updated total money
        print(n,"============================================================.") #prints seperation line
        n+=1 #increases the line count by 1
    elif dealerRoll > userRoll: #else if statment to check if the dealers roll is larger than the users roll
        userMoney -= betAmount #adds the bet amount to the dealers money
        dealerMoney+= betAmount #subtracts the bet amount from the users money
        print("You lost! You now have $"+str(userMoney)+" dollars. The dealer has $"+ str(dealerMoney)+" dollars.") #prints a message that lets
        # the user know that they have lost money and displays both the users and dealers updated total money 
        print(n,"============================================================.") #prints seperation line
        n+=1 #increases the line count by 1
    if dealerMoney <=0 or userMoney <= 0: #if statement to check if either the dealer or user have no money or negative money(owe money)
        print("The game has ended. You have $"+str(userMoney)+" dollars and the dealer has $"+str(dealerMoney)+" dollars.")#prints a message that lets
        # the user know that either the user or dealer are out of money/owe money and that the game is now over
        print(n,"============================================================.") #prints seperation line
        n+=1 #increases the line count by 1
        print("Thank for playing the Rolling 2 Dice Game by Manuel Argueta!")#farewell message from author
        print(n,"============================================================.") #prints seperation line
        x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then ENTER to exit: ") #gives users instructions on how to exit the program
        break #stops the while loop when either the dealer or user have 0 or negative money
        #End of MAIN Program ===============================================================================
