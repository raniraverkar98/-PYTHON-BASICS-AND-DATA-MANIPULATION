a=int(input("Enter the First No: "))
b=int(input("Enter the Second No: "))
z=0
print("A For Addition: ","S For Substraction: ","M For Mutliplication: ","D For Division: ")
Result=input("Enter your Choice: ")
if Result=="A":
    z=a+b
    print("Addition is: ",z)
elif Result=="S":
     z=a-b
     print("Substraction is: ",z)
elif Result=="M":
     z=a*b
     print("Multiplication is: ",z)
elif Result=="D":
     z=a/b
     print("Division is: ",z)
else:
     print("Invalid Choice")     




