#===========================================================================.
#Author: Manuel Argueta
#Date: 11/04/2020
#Purpose: The following program that will accept 3 integer numbers from the user, and will
#output these 3 numbers in ascending order, the sum of the 3 numbers , and the average 
#of these 3 numbers

#START of def Max
def Max(p,q,r):
    if p >= q and p >= r : #if statement to check if p is larger than or equal to q and r
        return p #returns value p
    elif q >= p and q >= r: #elseif statement to check if q is larger than or equal to p and r
        return q #returns value q
    else: #if none of the other statements are true it returns r
        return r #returns value r
#END of def Max

#START of def Min
def Min(p,q,r):
    if p <= q and p <= r: #if statement to check if p is less than or equal to q and r
        return p #returns value p
    elif r <= q and r <= p: #else if statement to check if r is less than or equal to q and p
        return r #returns value r
    else: #if none of the other statements are true it returns q
        return q #returns value q
#END of def Min

#START of def Mid
def Mid(p,q,r):
    if q <= p and p <= r or r <= p and p <= q: #if statement to check if p is greater than q and less than r
    #or if p is greater than r and less than q
        return p #returns value p
    elif q <= r and r <= p or p <= r and r <= q: #if statement to check if r is greater than q and less than p
    #or if r is greater than p and less than q
        return r #returns value r
    else: #if none of the other statements are true it returns q
        return q #returns value q
#END of def Mid

#START of def Sum
def Sum(p,q,r):
    return p + q + r #adds p, q and r and returns the value
#END of def Sum

#START of def Avg
def Avg(p,q,r):
    return Sum(p,q,r)/3 #divides the sum of (p,q,r) by 3 and returns the value
#END of def Avg

#MAIN Program=======================================================================================
n = 1 #intializes variable n to keep track of line numbers
print("Welcome to the Number Game by Manuel Argueta!") #welcome message to user from author
print(n,"---------------------------------------------------------------------------------.") #prints 
#seperation line with line number
n+=1 #increase line number by one
#start of whiel loop
while True: 
    p = int(input("Enter your first number: ")) #prompts user to enter an integer and stores it in variable p
    q = int(input("Enter your second number: ")) #prompts user to enter an integer and stores it in variable q
    r = int(input("Enter your third number: ")) #prompts user to enter an integer and stores it in variable r
    if p == -777: #if statement to checlk if p is equal to -777
        print(n,"---------------------------------------------------------------------------------.") #prints 
        #seperation line with line number
        n+=1 #increase line number by one
        print("Thank you for playing this Number Game by Manuel Argueta!") #farewell message to user from author
        print(n,"---------------------------------------------------------------------------------.")#prints 
        #seperation line with line number
        break #break statement to stop the while loop 
    print("You just entered three integers: " + str(p) + ', ' + str(q) + ', ' + str(r)) #prints the three 
    #integers that the user entered (p,q,r)
    sum = Sum(p,q,r) #stores the sum of the three numbers in variable sum
    avg = Avg(p,q,r) #stores the sum of the three numebers in variable avg
    max = Max(p,q,r) #stores the maximum or largest number of p, q, r in variable max
    min = Min(p,q,r) #stores the minimum or smallest number of p, q, r in variable min
    mid = Mid(p,q,r) #stores the middle or intermediate number of p, q, r in variable mid
    print("These three integers in order are: " + str(min) + ', ' + str(mid) + ', ' + str(max)) #prints the 
    #p, q, r in order ( min -> max) by printing variables min, mid and max
    print("The sum of these three numbers is: " + str(sum) + " and their average is: " + str(avg) + " .") #prints
    #the sum of p, q, and r and the average by printing variables sum and avg.
    print(n,"---------------------------------------------------------------------------------.") #prints 
    #seperation line with line number
    n+=1 #increase line number by one
#END of MAIN PROGRAM========================================================================================
