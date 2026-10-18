# Student management system
class student:
    def __init__(self,name,age,course,marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_info(self):
            print(f"Name:{self.name}")
            print(f"Age:{self.age}")
            print(f"Course:{self.course}")
            print(f"Marks:{self.marks}")

    def is_pass(self):
     
     if self.marks >= 40:
          return True
     else:
          return False
student1 = student("Swatantra",18,"BCA",65)
student2 = student("Pradyuman",17,"BCA",95)
student3 = student("Arjun",18,"BCA",65)
student4 = student("Shivansh",19,"BCA",30)
students=[student1 , student2 , student3,student4]
for s in students:
    s.display_info()
    if s.is_pass():
        print("Pass")
    else:
        print("Fail")
search_name = input("Enter student name:") 
found = False
for s in students:
    if s.name == search_name:
        s.display_info()
        found = True
        break
if not found:
     print("Data not found")


         






