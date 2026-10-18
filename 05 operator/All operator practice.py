
# Weekend checker
def weekend_checker():
    a=input("Enter day: ")
    if(a== "Saturday" or "sunday" or "saturady" or "sunady"):
        print("weekend")
    else:
        print("Weekday")
#Hot & Humid
def hot_humid():
    a=int(input("Enter temperature: "))
    b=int(input("Enter humid: "))
    if(a>25 and b>60):
        print("Hot and Humid")
    else:
        print("Not hot and Not humid")
#Logical combination 
def logical_combination():
    a=int(input("Enter your age: "))
    b=input("Do you have ID (Yes,No)?: ")
    c=input("Are you member of group (Yes,No)?: ")
    if((a>=18 and b=="Yes")or c=="Yes"):
        print("You asre eligble")
    else:
        print("Not eligble")
#Student Eligibility System 🎓
def eligibility_System():
    a=int(input("Enter your age: "))
    b=int(input("Enter your marks: "))
    if(a>=18 and b>=40):
        print("You are eligble")
    else:
        print("Not eligble")
#login system 
def login_system():
    a = "admin"
    b = "1234"
    c = input("Enter your user name: ")
    d = input("Enter your password: ")
    if(c==a and d==b):
        print("Login sucessfull")
    else:
        print("Login failed")
login_system()
