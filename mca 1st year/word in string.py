def findword(str,word):
    if word in str:
        return "found"
    else:
        print("not found")


str1 = input("enter the str :  ")
word1 = input("enter the word :   ")

result = findword(str1,word1)
print(result)