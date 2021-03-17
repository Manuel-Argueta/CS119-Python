#============================================================================================
#Author: Manuel Argueta 
#Date: 10/13/20
#Purpose: The following programs takes 2 numbers(as input) form the user and can perform any of the 
# 6 operations: addition, subtraction, multiplication, floating-point division, exponentation, and 
# division remainder (the operator is also inputed by user)

#MAIN Program=================================================================================
n = 1 #initilaizes variable n to keep track of line numbers
print("Welcome to the Simple Calculator of Manuel Argueta!") #greets user with porgam name and author
print(n,"================================.") #prints seperation line(w/line number)
n+=1 #increase line number by 1
#start of while loop
while True:
    output = 0 #initializes variable output(with the value of 0) which will store the ouput of the operation 
    n1 = float(input("Enter the first number: ")) #prompts user to enter the first number that will be used
    #in operation`
    op = str(input("Enter the operator (@ to stop): ")) #prompts user to enter operand to determine operation
    n2 = float(input("Enter the second number: ")) #prompts the user to enter the second number that will be used
    #in operation
    if op == "@": #if statement to check if the operator entered is the @ symbol
        print(n,"================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
        print("Thank you for using this Simple Calculator by Manuel Argueta!") #farewell/thank you message for
       #user from author
        print(n,"================================.") #prints seperation line(w/line number)
        break #ends while Loop and the program
    if op != '+' and op != '-' and op != '*' and op != '/' and op != '**' and op != '%' and op != '//': #if statement to
        #check if the inputed operatopr is any of the valid ones(+,-,*,/,**,%)
        print("Sorry, " + str(op) + " is not a valid operator!") #message to let user know that the 
        #operator they entered is not a valid one
        print(n,"================================.") #prints a seperation line(w/line number)
        n+=1 #increases line number by 1
    elif op == '+': #if statement to check if the inputed operator is the plus sign
        output = n1 + n2 #adds the 2 numbers the user has inputed
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
    elif op == '-': #if statement to check if the inputed operator is a minus sign
        output = n1 - n2 #subtracts the 2 numbers the user inputed(n1-n2)
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.") #prints seperation line(w/line number )
        n+=1 #increases line number by 1
    elif op == '*': #if statement to check if the inputed operator is an asterisk(multiplication)
        output = n1 * n2 #multiplies the 2 numbers the user has inputed
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    elif op == '/' and n2 == 0 or op == '%' and n2 == 0 or op == '//' and n2 == 0: #if statement to check
        #if the user has entered the second number(n2) as 0 and the operator as /, % or //
        print("The second number cannot be zero!") #prints message to let the user know that when using
        #division, modulus, or integer divison n2(the second number) cannot be 0
        print(n,"================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1
    elif op == '/' and n2 != 0 : #if statement to check if the inputed operator is a forward 
        #slash(division) and n2 not equal to 0
        output = n1 / n2 #divides the 2 numbers the user inputed(n1/n2)
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    elif op == '**': #if statement to check if the inputed operator is 2 asteriks(exponent)
        output = n1 ** n2 #gives output the value of n1 to the power of n2 (n1**n2)
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.") #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    elif op == '%' and n2 != 0:  #if statement to check if the inputed operator is a percent
        #sign(modulus) and n2 not equal to 0
        output = n1 % n2  #divides the 2 numbers the user inputed and gives output the value of 
        #the quotient(n1%n2)
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
    elif op == '//' and n2 != 0:  #if statement to check if the inputed operator is 2 forward 
        #slashes(integer division) and n2 not equal to 0
        output = n1 // n2  #divides the 2 numbers the user inputed using integer division(n1//n2)
        print("Result: " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(output)) #prints the 
        #result of the calculation
        print(n,"================================.")  #prints seperation line(w/line number)
        n+=1 #increases line number by 1 
# END OF MAIN Program========================================================================
