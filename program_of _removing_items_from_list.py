# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#      Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#      Expected Output : ['Green', 'White', 'Black']


colorList=["Red","Green","White","Black","Pink","Yellow"]

colorList.pop(0)
colorList.pop(3)
colorList.pop(3)
print(colorList)
