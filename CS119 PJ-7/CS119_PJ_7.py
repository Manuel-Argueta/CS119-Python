#============================================================================================
#Author: Manuel Argueta 
#Date: 10/13/20
#Purpose: The following programs takes 2 numbers(as input) form the user and can perform any of the 
# 6 operations: addition, subtraction, multiplication, floating-point division, exponentation, and 
# division remainder (the operator is also inputed by user)
#START of def add
def add(n1,n2):
    output = n1 + n2 #adds the 2 numbers the user has inputed
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def add

#START of def subtract
def subtract(n1,n2):
    output = n1 - n2 #subtracts the 2 numbers the user inputed(n1-n2)
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def subtract

#START of def multiply
def multiply(n1,n2):
     output = n1 * n2 #multiplies the 2 numbers the user has inputed
     print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
     #result of the calculation
#END of def multiply

#START of def divide
def divide(n1,n2):
    while n2 == 0:
        n2 = float(input("Enter your second number which cannot be zero: "))
    output = n1 / n2 #divides the 2 numbers the user inputed(n1/n2)
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def divide

#START of def power
def power(n1,n2):
    output = n1 ** n2 #gives output the value of n1 to the power of n2 (n1**n2)
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def power

#START of def modulus
def modulus(n1,n2):
    while n2 == 0:
        n2 = float(input("Enter your second number which cannot be zero: "),)
    output = n1 % n2  #divides the 2 numbers the user inputed and gives output the value of 
    #the quotient(n1%n2)
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def modulus

#start of def intDivision
def intDivision(n1,n2):
    while n2 == 0:
        n2 = float(input("Enter your second number which cannot be zero: "))
    output = n1 // n2  #divides the 2 numbers the user inputed using integer division(n1//n2)
    print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
    #result of the calculation
#END of def intDivision
    
#MAIN Program=====:
#============================================================================
n = 1 #initilaizes variable n to keep track of line numbers
print("Welcome to the Super Calculator of Manuel Argueta!") #greets user with program name and author
print(n,"======================================.") #prints seperation line(w/line number)
n+=1 #increase line number by 1
#start of while loop
while True:
    output = 0 #initializes variable output(with the value of 0) which will store the ouput of the operation 
    n1  = float(input("Enter the first number: ")) #prompts user to enter the first number that will be used
    #in operation`
    op = str(input("Enter the operator (@ to stop): ")) #prompts user to enter operand to determine operation
    n2 = float(input("Enter the second number: ")) #prompts the user to enter the second number that will be used
    #in operation
    if op == "@": #if statement to check if the operator entered is the @ symbol
        print(n,"======================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
        print("Thank you for using this Super Calculator by Manuel Argueta!") #farewell/thank you message for
        #user from author
        print(n,"======================================.") #prints seperation line(w/line number)
        break #ends while Loop and the program
    #while loop to check if entered operator is valid or not; if it isn't it will continue to ask for a valid one
    while op != '+' and op != '-' and op != '*' and op != '/' and op != '**' and op != '%' and op != '//':
        op = str(input("Please enter a valid operator: "))
    if op == '+': #if statement to check if the inputed operator is the plus sign
        add(n1,n2) #calls function add
        print(n,"======================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
    if op == '-': #if statement to check if the inputed operator is a minus sign
        subtract(n1,n2) #calls fucntion subtract
        print(n,"======================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
    if op == '*': #if statement to check if the inputed operator is an asterisk(multiplication)
        multiply(n1,n2) #calls function multiply
        print(n,"======================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    if op == '/': #if statement to check if the inputed operator is a forward 
        divide(n1,n2) #calls function divide
        print(n,"======================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    if op == '**': #if statement to check if the inputed operator is 2 asteriks(exponent)
        power(n1,n2) #calls function power
        print(n,"======================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    if op == '%':  #if statement to check if the inputed operator is a percent
        modulus(n1,n2) #calls function modulus
        #sign(modulus) and n2 not equal to 0
        print(n,"======================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    if op == '//':  #if statement to check if the inputed operator is 2 forward 
        intDivision(n1,n2) #calls function intDivision
        #slashes(integer division) and n2 not equal to 0
        print(n,"======================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
# END OF MAIN Program========================================================================

