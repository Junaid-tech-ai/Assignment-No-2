# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

num=int(input('Enter the number: \n'))
def number_difference (num):
    if num> 17:
        difference=num-17
        return 2*difference
    else:
        differnce=17-num
        return differnce
result_difference=number_difference(num)
print("The result of difference is =", result_difference)