#Report card
#input:student name
#output:marks ,average,grade

#to clear screen
import os

class Student:

    #stores data in variable
    def __init__(self,name,maths,science,english):
        self.name=name
        self.maths=maths
        self.science=science
        self.english=english

    # calculates average
    def average(self):
        return (self.maths+self.science+self.english)/3

    #calculates grade
    def grade(self):
        avg=self.average()
        if avg >= 90 :
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "F"

    #display marks average grade0
    def display(self):
        print("Maths   : ",self.maths)
        print("science : ",self.science)
        print("English : ",self.english)
        print("-"*25)
        print(f"Average : {self.average():.2f}")
        print("Grade   : ",self.grade())
        print("-"*25)


        
#clears screen
os.system('cls' if os.name == 'nt' else 'clear')


#updates marks
alex=Student("alex",80,72,91)
maxim=Student("maxim",99,92,53)
thor=Student("thor",10,23,24)


#prints a nice title
print("="*25)
print("REPORT CARD".center(25))
print("="*25)


#asks name
nam=input("ENTER YOUR NAME:").lower()

#print a horizontal line
print("-"*25)   


#control flows into class according to student name
if nam == "alex":
    alex.display()
elif nam == "maxim":
    maxim.display()
elif nam== "thor":
    thor.display()
else:
    print(f"there is no student named {nam}. ")
    
print("\n"*3)

#THE END
