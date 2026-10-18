#Basic thinking
def Basic_thinking():
    i=1
    while(i<=5):
        print(i)
        i+=1
# Reverse counting using while loops
def Reverse_countining():
    i=5
    while(i>=1):
        print(i)
        i-=1
# Print Even Numbers Between 1-20
def Even_number():
    i=1
    while(i<=20):
        if(i%2==0):
            print("Even number",i)
        i+=1
# Print Numbers from 1 to N
def print_number():
    print("We are representing number")
    n=int(input("Enter your number: "))
    i=1
    while(i<=n):
        print(i)
        i+=1
# Sum of Numbers from 1 to N
def sum():
    n=int(input("Enter your number: "))
    i=1
    total=0
    while(i<=n):
        total=total+i
        i+=1
    print("Sum",total)
# Password retry system
a=("python123")
b=input("Please enter your correct password: ")
while(a!=b):
    if(a!=b):
        print("Retry")
    b=input("Enter again: ")

print("Succesful")
    