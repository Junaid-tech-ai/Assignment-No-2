# Print the following patterns using loop :
# a.
# *
# **
# ***
# ****
row=4 # range will be range(1,5), because 5 no include in range
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end="")
    print()
