# Write a program which should count Vowels in the strings and return vowels in reverse order.
string=str(input("Enter the String: \n"))
count=0
vowelList=[]
def count_Vowels(string):
    vowels=["a","e",'i',"o","u"]
    for character in string:
        if character in vowels:
            count +=1
            vowelList.append(character)
    return count
print(count)



