# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum

num1=int(input('Enter the First Number :\n'))
num2=int(input('Enter the 2nd Number :\n'))
num3=int(input('Enter the 3rd Number :\n'))

def calculate_sum(num1,num2, num3):
    sum=num1+num2+num3

    if num1==num2==num3:
        return 3*sum
    else:
        return sum
result=calculate_sum(num1,num2,num3)
print("The sum of given Three numbers", result)