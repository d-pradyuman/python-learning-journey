#calculator
a =int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
# Which type of calculation you wish to perform 
operation = input("Which type of calculation you wish to perform,(+,-,*,/,%,**,Percentage)?:")
if(operation=="+"):
    print(a+b)
elif(operation=="-"):
    print(a-b)
elif(operation=="*"):
    print(a*b)
elif(operation=="/"):
    print(a/b)
elif(operation=="%"):
    print(a%b)
elif(operation=="**"):
    print(a**b)
elif(operation=="Percentage"):
    print(a/b*100)
else:
    print("Invalid operation")
    
