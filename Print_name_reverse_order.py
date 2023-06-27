# Write a Python program which accepts the user's first and last name and print them in ' \
# reverse order with a space between them


firstName=str(input("Enter the First Name: \n"))
lastName=str(input("Enter the Last Name: \n"))

fullName=lastName + " " + firstName
print("Reverse name is = ",fullName)