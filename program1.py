name = input("Enter Name: ")
dob = input("Enter Date of Birth: ")
usn = input("Enter USN: ")
dept = input("Enter Department: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("DOB:", dob)
print("USN:", usn)
print("Department:", dept)

print("\nTotal Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Message: Excellent")
elif percentage >= 75:
    print("Message: Very Good")
elif percentage >= 50:
    print("Message: Good")
else:
    print("Message: Needs Improvement")
