print("Student Grade Report")

Name = input("Enter your Name: ")
Roll = input("Enter your Roll No: ")

Chem = int(input("Enter your Chemistry Marks: "))
Phy = int(input("Enter your Physics Marks: "))
Bio = int(input("Enter your Biology Marks: "))

Total = Chem + Phy + Bio
print("Your Total Marks:", Total)

Avg = Total / 3
print("Your Average Marks:", Avg)