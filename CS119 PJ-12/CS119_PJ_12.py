#=============================================================================================
#Author: Mnauel Argueta
#Date: 12/11/20
#Purpose: The following program that will accept a list of integers (20 maximum) from the user, it will then show 
#those numbers in ascending order, it will show the sum of all integers, and
 
#START of def swap
def swap(list,i,j): #the function swap takes the parameters list,i and j. Parameter list is the list where the function will
#swap tow elements, i and j are teh two elements that are being swapped(i becomes j and j becomes i) 
    temp = list[i] #initializes variable temp to temporarily hold the original value of list[i]
    list[i] = list[j] #changes the element at position list[i] to the element at list[j]
    list[j] = temp #changes the element at position list[j] to the value held in variable temp(original value of lis[i])
    return list #returns the changed list with swapped elements
#END of def swap

#START of def binarySearch
def binarySearch(target,list): #the function swap takes the parameters list and target. Parameter list is the list that the 
#function that will search for parameter target.
    low = 0 #initializes variable low to the value of 0 to show that the lowest index is 0 
    mid = 0 #initializes variable mid to the value of 0 to determine the middle index of the list
    high = len(list) - 1 #initializes variable high to the highest index in list(the length of the list minus one)
    while low <= high: #start of while loop that will continue as long as low is less than or equal to high
        mid = (high+low)//2 #gives variable mid the value of the lowest index plus the highest index divided by two(using
        #integer division) to get the lists middle index
        if list[mid] < target: #if statement to check if the number at list[mid] is smaller than the target
            low = mid + 1 #increases the value of low by 1(moves to next element after the lowest index)
        elif list[mid] > target: #if statement to check if the number at list[mid] is larger than the target
            high = mid -1 #decreases the value of high by 1(moves to next element before the highest index)
        else: #if none of the previous if statements were true its will execute this
            return mid #returns the index stored at mid(the location of the target)
    return -1 #if the target is not found the function returns -1
#END of def binarySearch

#START of def selectionSort
def selectionSort(list): #the function selectionSwap takes the parameters list. Parameter list is the list that the 
#function will sort
    for i in range(len(list)-1): #for loop to loop through all the indexes of list
        min = i #initiates variable min to the value of i
        for j in range(i+1,len(list)): #for loop to go through the elements after i to the length of the list 
            if list[j] < list[min]: #if statement to check if the element at list[j] is less than list[i]
                min = j #gives the variable min to j 
        swap(sList,i,min) #calls function swap to swap the element that is at position i to the element in position j
#END of def selectionSort

#START of def Sum
def Sum(list): #the function Sum takes the parameter list. Parameter list is the list that fucntion will be adding
    sum = 0 #initiates variable sum to the value of 0
    for i in range(len(list)): #for loop to loop through every element of list
        sum += list[i] #adds element i to the value of sum
    return sum #returns variable sum 
#END of def sum

#START of def average
def average(list): #the function Sum takes the parameter list. Parameter list is the list that fucntion will be calculating
#the average of
    average = 0 #initiates variable average to the value of 0
    average = Sum(list)/len(list) #calculates the average value of the list by calling function Sum and dividing it by
    #the length of the list and staores it in variable average
    return average #returns variable average
#END of def average

#MAIN PROGRAM=================================================================================
n = 1 #initiates varaible n  to the value of 1 to keep track of the line numbers
print("Welcome to the List Sorting and Searching Game of Manuel Argueta!") #prints a welcome message from the author
while True: #start of while loop
    print(n,"=========================================================.") #prints a seperation line with a line number
    n+=1 #increases the line number by 1
    listLen = int(input("Please enter how many integers you would like to input(up to 20, enter 0 to stop): ")) #initiates the variable listLen
    #to the value that the user inputs. listLen is the length of the list
    while listLen < 0 or listLen > 20: #while loop to continue asking for the user to input the lists length until they input an integer greater than
        #0 and less than 20 
        listLen = int(input("Please enter how many integers you would like to input(up to 20, enter 0 to stop): ")) #asks the user to enter the lists length 
    if listLen == 0: #if statement to check if the user inputed listLen as 0
        print(n,"=========================================================.") #prints a seperation line with a line number
        n+=1 #increases the line number by 1
        print("Thank you for playing the List Sorting and Searching Game by Manuel Argueta") #prints a farewell message from the author
        print(n,"=========================================================.") #prints a seperation line with a line number
        break #stops the main while loop
    sList = [] #initiates an empty list names sList
    for i in range(listLen): #for loop to loop the length of the list that the user wants created
        inputedInt = int(input("Please enter the integer you would like to add to the list: ")) #asks user to input an intger that
        #they would like to add into sList and stores it in inputedInt
        sList.append(inputedInt) #appends inputedInt to sList
    selectionSort(sList) #calls function selectionSort to sort sList
    print("Your " + str(listLen) + " integers in ascending order are: ", end = "") #prints a frame sentence to let the the user know the program will 
    #print the inputed integers in ascending order
    for j in range(0,listLen): #for loop to loop through the indexes of sList
        print(sList[j],"",end ="") #prints the element at sList[j] on the same line
    print(" ") #prints a empty line to begin a new line
    print("The sum is: " + str(Sum(sList)) + ", and the average is: " + str(average(sList)))#prints a frame sentence to let the the user know the program will 
    #print the sum and average of sList
    print(n,"=========================================================.") #prints a seperation line with a line number
    n+=1 #increases the line number by 1
    while True: #start of while loop
        target = int(input("Please enter a number to search(enter -99 to end the search): ")) #initializes variable index and
        #asks the user to input the integer to look for
        if target == -99: #if statement to check if variable target is equal to -99
            break #ends/breaks the while loop
        index = binarySearch(target,sList) #initializes and gives variable index the value 
        if index != -1: #if statement to check if the index of the inputed target is not -1(this means the target was found)
            print("The number " + str(target) +" was found at position " +str(index+1)) #print a message to let the user know that the target they inputed was found 
            #at index
        elif index == -1: #if statement to check if the index of the inputed target is -1 
            print("The number " + str(target) + " was not found.")#if the index of target was -1
            #the number was not found and the program will print a message to let the user know of it
