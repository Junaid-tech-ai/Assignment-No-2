# Write a Python program to clone or copy a list.
newList=[]
parentList=[5,6,"56","46"]
# cloneList=parentList.copy()
for items in parentList:
    newList.append(items)
print(newList)