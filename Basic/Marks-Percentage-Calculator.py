print("Enter Your Marks\n")

Eng = int(input("Enter Your English Marks: "))
mat = int(input("Enter Your Maths Marks: "))
mar = int(input("Enter Your Marathi Marks: "))
comp =int( input("Enter Your Compurtr Marks: "))
sci = int(input("Enter Your Science Marks: "))

Tot = Eng + mat + mar + comp + sci
per = (Tot / 500) * 100


print("Total Marks is:", Tot)
print("Percentage is:", per)