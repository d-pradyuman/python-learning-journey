#basic tuple
number = (10,20,30,40,50,)
print("tuple:",number)
print("first element:",number[0])
print("last element:",number[-1])
#Tuple creation 
student=("Rahul",18,"Pyhon",)
student1="Rahul",18,"pyhon",
print(student)
print(student1)
#Indexing
colors=("red","green","blue","yellow","black")
print(colors[0])
print(colors[2])
print(colors[4])
#tuple unpacking
student=("Aman",20,"Python",)
Name,age,course=student
print("Name:",Name)
print("Age:",age)
print("Course:",course)
#Real world Problem
student=("Rahul",18,"Python","Delhi",)
Name,Age,Course,City=student
print(f"Name:{Name}\nAge:{Age}\nCourse:{Course}\nCity:{City}")
student1=("Pradyuman:",18,"Java","USA",)
Name,Age,Course,City=student1
print(f"Name:{Name}\nAge:{Age}\nCourse:{Course}\nCity:{City}")
#Python Tuples & Unpacking Practice
def get_student():
   student = ("Rahul", 18, "Python")
   return("Rahul", 18, "Python")
name, age, course = get_student()
print(f"Name:{name}\nAge:{age}\nCourse:{course}")
#Tuple Concatenation
data=(10,20,30,)
data1 = data + (40,)
print(data1)



