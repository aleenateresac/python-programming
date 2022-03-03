#program16
a=int(input("Enter the First number"))
b=int(input("Enter the second number"))
c=int(input("Enter the following numbers accordingly to perform corresponding operators \n 1.Adition \n 2.Substration \n 3.Multiplication \n 4.Division"))
if c==1:
    print("Sum of two numbers is",a+b )
elif c==2:
    print("Difference of two numbers is",a-b)
elif c==3:
    print("Product of two numbers is",a*b)
elif c==4:
    print("Quotient of two numbers is",a/b)
else:
    print("Invalid input")
