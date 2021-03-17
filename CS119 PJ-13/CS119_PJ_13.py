
#START of the definition of the Student class
class Student(object):
    #START of Student constructor method
    def __init__(self,studentID,lastName,firstName,gpa,phoneNum): #initializes each student object with a student id, last name
        #first name, gpa and phone number
        self.studentID = studentID #sets the students id to the inputed parameter studentID
        self.lastName = lastName #sets the students last name to the inputed parameter lastName
        self.firstName = firstName #sets the students first name to the inputed parameter firstName
        self.gpa = gpa  #sets the students gpa to the inputed parameter gpa
        self.phoneNum = phoneNum  #sets the students phone number to the inputed parameter phoneNum
    #START of Student constructor method

    #START of method getStudentID
    def getstudentID(self): 
        return self.studentID #returns the students id
    #END of method getStudentID

    #START of method getlastName
    def getlastName(self):
        return self.lastName #returns the students last name
    #END of method getlastName

    #START of method getfirstName
    def getfirstName(self):
        return self.firstName #returns the students first name
    #END of method getfirstName

    #START of method getGPA
    def getGPA(self):
        return self.gpa #returns the students gpa
    #END of method getGPA

    #START of method getphoneNum
    def getphoneNum(self):
        return self.phoneNum #returns the students phone number
    #END of method getphoneNum

    #START of method setstudentID
    def setstudentID(self,newID):
        self.studentID = newID #updates the students id by giving studentID the value of the newly inputed 
        #data in parameter newID
    #END of method setstudentID

    #START of method setlastName
    def setlastName(self,newlastName):
        self.lastName = newlastName #updates the students last name by giving lastName the value of the newly inputed 
        #data in parameter newlastName
    #END of method setlastName

    #START of method setfirstName
    def setfirstName(self, newfirstName):
        self.firstName = newfirstName #updates the students first name by giving firstName the value of the newly inputed 
        #data in parameter newfirstName
    #END of method setfirstName

    #START of method setGPA
    def setGPA(self, newGPA):
        self.gpa = newGPA #updates the students gpa by giving gpa the value of the newly inputed 
        #data in parameter newGPA
    #END of method setGPA

    #START of method setphoneNum
    def setphoneNum(self, newphoneNum):
        self.phoneNum = newphoneNum #updates the students phone number by giving phoneNum the value of the newly inputed 
        #data in parameter newphoneNum
    #END of method setphoneNum

    #START of method __str__ to print a string representation of Student
    def __str__(self):
        return "Student ID: " + str(self.studentID) + "\nLast Name: " + self.lastName + "\nFirst Name: " \
            + self.firstName + "\nGPA: " + str(self.gpa) + "\nPhone Number: " + self.phoneNum #called by function print to print every attribute of student(id, last name,
        #first name, gpa, and phone number in a series of formatted strings)
    #END of method __str__ to print a string representation of Student
#END of definition of Student class

#START of def main
def main():
    n = 1 #initializes the variable n to 1 to keep track of line numbers
    print("Welcome to the Student Report System by Manuel Argueta!") #prints a welcome message to the user from the author
    studentCount = 0 #initializes variable studentCount to the value of 0 to keep tracks of the total number of students
    totalGPA = 0 #initializes variable totalGPA to the value of 0 to store the total GPA of all students
    averageGPA = 0 #initializes variable averageGPA to the value of 0 to store the average GPA of all students
    j = 1  #initializes variable j to the value of 1 to keep track of the while loops iterations
    studentList = [] #initializes empty list studentList to keep track of all the students created
    while True: #start of while loop
        print(n,"===========================================.") #prints a seperation line and the line number
        n+=1 #increases line number by 1 
        if j == 1: #if statement to check if the while loop is on its first iteration
            ID = int(input("Please enter the first student's ID: ")) #asks the user to input the ID of the first student theyd like to create
        elif j > 1:#if statement to check if the while loop is its on any iteration after the 1st one
            ID = int(input("Please enter the next student's ID: ")) #asks the user to input the ID of the next student theyd like to create
        if ID == 0:
            print(n,"===========================================.")#prints a seperation line and the line number
            n+=1 #increases line number by 1 
            print("Thank you for using the Student Report System by Manuel Argueta!") #prints a farewell message to the user from the author
            print(n,"===========================================.")#prints a seperation line and the line number
            break #stops/breaks the while loop
        lastName = str(input("Please enter the student's last name: ")) #asks the user to input the last name of the student theyd like to create
        firstName = str(input("Please enter the student's first name: ")) #asks the user to input the first name of the student theyd like to create
        GPA = float(input("Please enter the student's GPA: ")) #asks the user to input the GPA of the student theyd like to create
        phoneNum = str(input("Please enter the student's phone number: ")) #asks the user to input the phone number of the student theyd like to create
        student = Student(ID,lastName,firstName,GPA,phoneNum) #creates a new Student object with the name of student and the 
        #properties that user previously inputed in variables ID, lastName, firstName, GPa, and phoneNum
        studentCount += 1 #increases the total number of students by 1
        totalGPA += GPA #adds the newly created students GPA to the total GPA
        averageGPA = totalGPA / studentCount #calculates the new average GPA 
        print("You just entered the following student record: ") #prints a sentence framework to let the user know that the program
        #will print the contents of the newly created student
        print(student) #prints student in a string form
        studentList.append([ID,lastName,firstName,GPA,phoneNum]) #appends the newly created student to list studentList
        print("========= CURRENT REPORT OF ALL STUDENTS ===============") #prints an start line to let the user know the current student report is starting
        print("Current Student Count: " + str(studentCount)) #prints the current amount of total students
        print("Total GPA Of All Students: " + str(totalGPA)) #prints the total gpa of the current total students
        print("Average GPA Of All Students: "+ str(averageGPA)) #prints the avaerage gpa of the current total students
        print("All Student Records Are As Follows: ") #prints a sentence framework to let the user know that the program will print the 
        #contents of studentList
        for i in studentList: #for loop to loop thorugh all the elements of student List 
            print(i) #prints i or the current element of studentList
        print("========= END OF REPORT =================================") #prints an end line to let the user know the current student report is over
        print(" ")
        j += 1 #increases the iteration counter by 1
#END of def main

if __name__ == "__main__": #if statement to check if the main function is defined 
    main() #calls main function
