# 1. Print the following pattern using for loop:
# A)
# **********
# **********
# **********
# **********
# B)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,5):
    for j in range(1,11):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
