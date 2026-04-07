name = input("Enter name: ")
yearofbirth = int(input("Enter year of birth: "))

age = 2026 - yearofbirth

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")