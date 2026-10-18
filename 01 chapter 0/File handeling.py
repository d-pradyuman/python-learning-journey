#read mode
file = open("chapter 0/Loops.py", "r")
content = file.read()
print(content)
file.close()
#written handiling
file = open("chapter 0/Loops.py", "w")
file.write("Hello, world!")
file.write("I am toppert.")
file.close()
#with ke saath
with open("chapter 0/Loops.py", "r") as file:
    content = file.read()
print(content)
