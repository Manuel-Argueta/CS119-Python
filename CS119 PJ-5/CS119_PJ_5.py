#=================================================================================
#Author: Manuel Argueta
#Date:10/06/20
#Purpose: The following program checks a password inputed by the user and prints all the violations of this password if any.

#MAIN Program=====================================================
n=1 #initializes varible that keeps track of line numbers
print("Welcome to the PASSWORD CHECKER by Manuel Argueta!") #introduces user with author and program name
print(n,"============================================================.") #creates division line
n+=1 #increases line number by 1
#start of while loop
while True: 
    errorCount = 0 #initializes variable to keep track of # of errors or 
    upperCaseCount = 0 #initializes variable to keep track of the number of uppercase letters in password
    lowerCaseCount = 0 #initializes variable to keep track of the number of lowercase letters in password
    digitCount = 0 #initializes variable to keep track of the number of digits in password
    specialCharCount = 0 #initilaizes variable to keep track of the special characters in in password
    yearCount = 0 #initilaizes variable to keep track of how many times a certain year is in password
    password = str(input("Please enter a password (ENTER q TO QUIT): ")) # gets the test password from the user
    if password == "q": #if statement to check if password inputed is the letter'q'
        print(n,"============================================================.") #creates division line
        n+=1 #increases line number by 1
        print("Thank you for using the PASSWORD CHECKER by Manuel Argueta!") #gives user a farewell and thank you
        print(n,"============================================================.")#creates division line
        break #stops the program
    print('The password you entered is: "' + str(password) + '" ') #prints the inputed password
    upperLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #defines list upperLetters which contains the uppercase alphabet
    for i in upperLetters: #for loop to run through each element in upperLetters
        upperCaseCount += password.count(i)# adds 1 to upperCaseCount when one of the elements in list upperLetters
        # is found in the inputed password
    if upperCaseCount < 2: #if statement to check if password has at least 2 upper case letters
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R1: Your password is not secure because it has less than 2 upper-case letters.")
        #notifies user of a violation(specifies the violation)
    lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #defines list lowerLetters which contains the lowercase alphabet
    for k in lowerLetters: #for loop to run through each element in lowerLetters
        lowerCaseCount += password.count(k)# adds 1 to lowerCaseCount when one of the elements in list lowerLetters
        # is found in the inputed password
    if lowerCaseCount < 2: #if statement to check if password has at least 2 lower case letters
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R2: Your password is not secure because it has less than 2 lower-case letters.")
        #notifies user of a violation(specifies the violation)
    if len(password) < 7: #if statement to check if password has at least 7 characters
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R3: Your password is not secure because it has less than 7 characters.")
        #notifies user of a violation(specifies the violation)
    digits = ['0','1','2','3','4','5','6','7','8','9',]
    #defines list digits which contains all of the digits
    for l in digits: #for loop to run through each element in digits
        digitCount += password.count(l)# adds 1 to digitCount when one of the elements in list digits
        # is found in the inputed password
    if digitCount < 2: #if statement to check if password has at least 2 digits
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R4: Your password is not secure because it has less than 2 digits.")
        #notifies user of a violation(specifies the violation)
    if len(password) > 12: #if statement to check if password has more than 12 characters
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R5: Your password is not secure because it has more than 12 characters.")
        #notifies user of a violation(specifies the violation)
    if password.count(' ') > 0: #if statement to check if password has any spaces
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R6: Your password is not secure because it contains space.")
        #notifies user of a violation(specifies the violation)
    if password.isdigit(): #if statement to check if password is made up of only digits
        errorCount+= 1 #adds one to the error count(total rule violations)
        print("ERROR R7: Your password is not secure because it contains only digits.")
        #notifies user of a violation(specifies the violation)
    if password.isalpha(): #if statement to check if password is made up of only letters
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R8: Your password is not secure because it contains only letters.")
        #notifies user of a violation(specifies the violation)
    specialChars = ['$','%','@','!','?','*',]
    #defines list specialChars which contains the 6 possible special characters
    for s in specialChars: #for loop to run through each element in upperLetters
        specialCharCount += password.count(s)# adds 1 to specialCharCount when one of the elements in list specialCharCount
    if specialCharCount == 0: #if statement to check if password has at least 1 special character
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R9: Your password is not secure because it doesn't contain any special charcters: $,%,@,!,?,*")
        #notifies user of a violation(specifies the violation)
    yearCount += password.count("2020") + password.count("2019") + password.count("2018") + password.count("2017") 
    #adds 1 to variable yearCount everytime any of the 4 years appear in password
    if yearCount > 0: #if statement to check if password has '2020','2019','2018',or '2017'
        errorCount += 1 #adds one to the error count(total rule violations)
        print("ERROR R10: Your password is not secure because it contains 2020, 2019, 2018, or 2017.")
        #notifies user of a violation(specifies the violation)
    if errorCount == 1: #if statement to check if the # of errors made is 1
        print("Your password has " + str(errorCount) + " problem that needs to be fixed.")
        #prints message to let the user know they made 1 mistake.
    elif errorCount > 1: #if statement to check if the # of errors made is more than 1
        print("Your password has " + str(errorCount) + " problems that need to be fixed.")
        #prints message to let the user know they made more than one mistake.
    elif errorCount == 0: #if statement to check if the # of errors made is 0(no mistakes)
        print("Congratulations! Your password is very secure!")
        #prints message to let the user know that they have made no mistakes and have inputed a secure password.
    print(n,"============================================================.")#creates division line
    n+=1 #increases line number by 1
#END OF MAIN Program================================================================================================