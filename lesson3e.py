# BELLOW ISA GRADING SYSTEM BASED ON WHAT A STUDENT WILL HAVE GOTTEN.
marks = int(input("enter student marks: "))
# print("The entered marks is ", marks)
if marks  > 0 and marks < 30:
    print("Below Average")
elif marks >= 30 and marks < 40:
    print("Average")
elif marks >= 40 and marks < 70:
    print("Above Average")
elif marks >= 70 and marks <= 100:
    print("Excellent") 

else: 
    print("Invalid Input")