# Write a program which should count Vowels in the strings and return vowels in reverse order.
string=str(input("Enter the String: \n"))


def count_Vowels(string):
    i=0
    vowelList = []
    count=0
    vowels=["a","e",'i',"o","u"]
    for character in string:
        if character in vowels:
            count +=1
            vowelList.append(character)

    for i in range(len(vowelList),0,-1):
        print(vowelList[i-1])

count_Vowels(string)




