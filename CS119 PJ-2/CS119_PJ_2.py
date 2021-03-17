#============================================================.
#Author: Manuel Argueta
#Date: 09/23/20
#Purpose: The following program will print and compute a proffesional investment report based off of user input.

#MAIN PROGRAM
n = 1 # declaring a variable to track the number of seperation lines
print("Welcome to the Investment Report Tool by Manuel Argueta!")#introducing program name/purpose and author
print(n,"=====================================================.") #seperation line #1
n+=1#increases the line numbers by 1
investmentAmount = float(input("Enter the investment amount: "))#gets the initial investment amount from user
numYears = int(input("Enter the number of years: "))#gets the amount of years that the money will be invested from user
rate = float(input("Enter the rate as a %: "))#gets the interest rate for the investment in percent
rate = rate/100#divides interest by 100 to move the decimal two places to the right
print(n,"=====================================================.") #seperation line #2
n+=1#increases the line numbers by 1
print("%4s%18s%10s%16s" %  #formats the header for the investment report
("Year", "Starting Balance","Interest", "Ending Balance"))#prints the header for the investement report
endBalance = 0.0 #declares variable endBalance which tracks the investments final values after each year
                 #and at the end of the given number of years 
totalInterest = 0.0 #declares variable totalInterest which accumalates the interest gained from the investemnt over the given
                    #number of years
interest = 0.0 #declares variable interest to keep track of the interest gained every year 
for year in range(1,numYears+1): #for loop to perform the investment calculation based on the number of years the user specified
    investmentAmount = investmentAmount + interest #give the investment amount the value of the investment amount and interest
    interest = investmentAmount * rate #calculates the interest gained by multiplying the investment amount and interest rate
    endBalance = investmentAmount + interest #calculates the end balance of the investemnt over the years by adding the previous
                                             #investment amount and the interest of that year
    totalInterest += interest #calculates the total interest by adddding the interest gained each year
    print("%4d%18.2f%10.2f%16.2f" %  #formats the way the investment statistics are displayed
    (year, investmentAmount, interest, endBalance)) #prints the yearly investment statistics; the year, investment amount, interest
                                                    #and the ending balance
print(n,"=====================================================.") #seperation line #3
n+=1#increases the line numbers by 1
print("Ending Balance: $%0.2f" % endBalance) #prints the ending balance of the investment after the given number of years
print("Total Interest Earned: $%0.2f" % totalInterest) #prints the total amount of interest earned in the given amount of years 
print(n,"=====================================================.")#seperation line #4
n+=1#increases the line number by 1
print("Thank you for using the Investment Report Tool by Manuel Argueta!")#greets the user goodbye letting teh user know the programs 
                                                                          #use is over
print(n,"=====================================================.")#seperation line #5
x = input("Press Ctrl+Alt+PrtScn to get a snapshot of this console, then Enter to exit: ")
 # End of MAIN PROGRAM
