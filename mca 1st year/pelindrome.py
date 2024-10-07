# Write a program to reverse given String and check whether it is a Palindrome or not?
def palindrome(n):
    strreverse = str(n)[ : : -1]
    if strreverse == str(n):
        return True
    else:
        return False
num = int(input("enter your number to check palindrome : "))
result = palindrome(num)
print(result)

 
# 40 Write a program to reverse given String and check whether it is a Palindrome or not?

def strpalindrome(str):
    reversestr = str[: : -1]
    if str == reversestr:
        print("its palindrome ")
    else:
        print("its not")
str1 = str(input("enter the string : "))
strpalindrome(str1)