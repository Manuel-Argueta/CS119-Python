#Author: Manuel Argueta
#Date: 09/08/2020
#Purpose: CS119 PJ-1 This program createsa console based game where the user adds 3 numbers and earns/loses points for each win/loss.

def testAdd(num1,num2,num3): #defines function testAdd, 3 parameters from caller(three numbers)
    points =10 #10points for each win
    sum = int(input("Please enter the sum of the 3 numbers you entered: "))#gets users attempt at sum of 3 numbers
    if sum==(int(num1)+int(num2)+int(num3)): #if statemnt to check if the sum entered was correct or not
        print("You got it right! You earned: "+ str(points)+ " points!")
        list[0]+=points #adds points to the users total score
        print("Therefore you have " + str(list[0])+ " total points!") #tells user total amount of points
    else: 
        print("That sum was incorrect! You lost "+str(points)+" points.")
        list[0]-=points
        print("Therefore you have " + str(list[0])+ " total points!") #tells user total amount of points
#MAIN PROGRAM
total_points = 0 #creates a variable to store users total amount of points
list = [total_points] #one element list to make sure total_ponits to update all functions
print("Welcome to the Number Adding Game of Manuel Argueta.")#greets and introduces author to user
user_name=input("Enter your first and last name: ")
print(str(user_name)+", lets start playing! You have "+ str(list[0])+" points to start with.")
while True:
    num1 = input("Enter your first number: ") #string num1
    num2 = input("Enter your second number: ") #string num2
    num3 = input("Enter your third number: ") #string num3
    testAdd(num1,num2,num3)#calling function testAdd to check if the user answered correctly or not
    continue_playing = input("Would you like to continue playing? Enter 'yes' to continue & 'no' to exit: ")#get players input about continuing to play
    if continue_playing == "no": #if statement to check if player said yes or no
        break
print("Thank you for playing the Number Adding Game by Manuel Argueta!")
x = input("Press Ctrl+Alt+PrtSc to take a screenshot of the console and ENTER to exit")
#END of MAIN PROGRAM