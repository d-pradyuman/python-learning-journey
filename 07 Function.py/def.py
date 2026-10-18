# Q1 -- Create and Call a Simple Function
def greet():
    print("Hello, Python!")
greet()
#  Q2 — Function to Display a Name
def show_name():
    print("My name is Pradyuman Dubey")
show_name()
# Q3 — Function to Print Numbers
def show_number():
    n=1
    while(n<=5):
        print(n)
        n+=1
show_number()
# Q4 — Function with a Parameter
def greet_user(Pradyuman):
    print("Hello!",Pradyuman)
greet_user("Pradyuman")
# Q5 — Square of a Number Using Function
def square(number):
    return number*number
print(square(1599753))
# Q6 — Addition of Two Numbers Using Function
def add(a,b):
    return a+b
print(add(50,60))
# Q7 — Calculate Rectangle Area.
def Area(Length,Breath):
    return Length*Breath
print("Area: ",Area(10,38))
# Q8 — Check Whether a Number is Even.
def is_even(number):
    return number%2==0
print("Number is even",is_even(10))
# Q9 — Calculate Total Price.
def calculate_total(Price,Quantity):
    return Price*Quantity
print("Total price: ",calculate_total(100,545))