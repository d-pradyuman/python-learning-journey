#Comparison operator
#comapre two number
a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
print("Equal:",a==b)
print("Not equal",a!=b)
print("First is greater:",a>b)
print("Firat is smaller:",a<b)
#Logical operator
#Code for driving eligbility test
age=int(input("Enter your age: "))
license=(input("Do you have license? (Yes/No): "))
if(age>=18 and license == "Yes"):
    print("You are eligble")
else:
    print("You are not eligble")