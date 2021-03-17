#============================================================================================
#Author: Manuel Argueta 
#Date: 11/11/20
#Purpose: The following programs takes 2 numbers(as input) form the user a   nd can perform any of the 
# 6 operations: addition, subtraction, multiplication, floating-point division, exponentation, and 
# division remainder (the operator is also inputed by user)


s1 = " "*10 #initialiazes variable s1 which is used in formatting
s2 = " "*12 #initialiazes variable s2 which is used in formatting
s3 = " "*13 #initialiazes variable s3 which is used in formatting
s4 = " "*9 #initialiazes variable s4 which is used in formatting
n = 1 #initializes variable n with the value of 1 to keep track of the line numbers
print("Welcome to the Loan Payment Report by Manuel Argueta!") #prints a welcome message introducing the author
print(n,"========================================================================.") #prints line number and 
#seperation line 
n+=1 #increases line count(n) by 1 
loanBalance = 1000.0 #initiates variable loanBalance (with a value of 1000) to keep track of how of the loan must be paid
annualInterestRate = 18.0 #initiates variable annualInterest to keep track of yearly interest rate
#(the value stored varies by test case)
interestRate = (annualInterestRate/12)/100 #gets the monthly interest rate by dividing the yearly interest rate by 12
#and turning it into a decimal by dividing it by 100
monthlyPayment = 180.0 #initiates variable monthlyPayment to keep track of the amount being "paid"(befor
#taking away interest)each month(this varies by test case)
monthNum = 0 #initiates variable monthNum to keep track of the month number
interestPaid = 0 #initiates variable interestPaid to keep track of the interest paid each month
debtPaid = 0 #initiates variable debtPaid to keep track of the amount taken away from the loan each 
#month(monthly payment minus the interest)
totalInterest = 0 #initiates variable totalInterest that will store the total amount of interest paid
print("Loan Amount: $" + str(loanBalance)+ "   Annual Interest Rate: " + str(annualInterestRate) + "%   Monthly Payment: $" + str(monthlyPayment))
#prints a header displaying the laon balance and annual intrest rate and the monthly payment
print(" ") #prints a blank line
print("%4s%18s%18s%14s%18s" % ("Month #","Month-Payment","Interest-Paid","Debt-Paid","Loan Balance"))
#prints a formatted header displaying the title of the 5 different columns
print("%4s%18s%18s%14s%18s" % ("-------","-------------","-------------","---------","------------"))
#prints a formatted underlining of each title of the 5 different columns
#start of while loop
while True:
    if loanBalance <= monthlyPayment: #if statement to check if the value stored in loanBalance is less
        #than the monthly Payment
        monthNum +=1 #increases monthNum by 1
        interestPaid = interestRate * loanBalance #gets the amount of interest paid that month by mulitpylying
        #the (monthly)interest rate by the loan blaance
        monthlyPayment = loanBalance + interestPaid #gets the monthly payment for the last month by adding the
        #required amount of interest and the remaining balance in loanBalance
        debtPaid = monthlyPayment - interestPaid #gets the amount paid off of the loan(interest not included)
        #by subtracting the interest paid from the monthly payment
        loanBalance -= loanBalance #makes the balance of the loan equal to 0
        totalInterest += interestPaid #adds the amount of interest paid that month to the total amount of interest paid
        print ("%-2d"% monthNum +s1+ "$%0.2f"%monthlyPayment +s2+ "$%0.2f"%interestPaid +s3+ "$%0.2f"%debtPaid +s4+ "$%0.2f"%loanBalance)
        #prints a formatted line with all 5 data sets(month number, montlhy payment, interest paid, debt paid and loan balance )
        print(" ") #prints a blank line
        print("Total Amount Of Interest Paid: $" + "%0.2f" % (totalInterest)) #prints a message displaying
        #the total amount of interest paid whilst paying the loan
        print(n,"========================================================================.") #prints line number
        #and a seperation line
        n+=1 #increases line number by 1
        print("Thank you for using the Loan Payment Report by Manuel Argueta!") #prints a farewell message from  
        #the author
        print(n,"========================================================================.") # orints line number and 
        #a seperation line
        break #breaks/stops the while loop and the program
    monthNum +=1 #increases the line number by 1
    interestPaid = interestRate * loanBalance #calculates the amount of interest paid that month by mulitplying
    #the interest rate and the loan balance
    debtPaid = monthlyPayment - interestPaid #calculates how much of the actual debt/loan is paid off by subtracting the 
    #interest paid from the monthly payment
    loanBalance -= debtPaid #calcuates the updated loan balance by subtracting teh debt apid from the loan balance
    totalInterest += interestPaid #adds the interest paid that month to the total interest
    print ("%-2d"% monthNum +s1+ "$%0.2f"%monthlyPayment +s2+ "$%0.2f"%interestPaid +s3+ "$%0.2f"%debtPaid +s4+ "$%0.2f"%loanBalance)
    #prints a formatted line with all 5 data sets(month number, montlhy payment, interest paid, debt paid and loan balance )  

