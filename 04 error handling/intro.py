
#Using try and except block
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("That was not a valid number.")

#Finally block
try:
    file = open('slicying.py', 'r')
    data = file.read()
except FileNotFoundError:
    print("The file was not found.")
finally:
    file.close()

#Rasing exceptional initially
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
