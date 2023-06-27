# Write a Python program to get the smallest number from a list.

numbersList=[50,60,90,80,15,20]
smallestNumber=numbersList[0]
for num in numbersList:
    if num<smallestNumber:
        smallestNumber=num
print("The smallest number is :", smallestNumber)