#Mini student result program
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if not (age >= 18 and marks >= 40):
    print("Not eligible")
else:
    print("You are eligible")
if(marks>=90):
    print("Excellent")
elif(marks>=60 and marks<=89):
    print("Good")
elif(marks>=40 and marks<=59):
    print("Pass")
else:
    print("Fail")



