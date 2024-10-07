#Write a Program tofind Factorial for given Number

n = int(input("enter the number :"))

def factorial(n):
    if n==0 or  n==1:
        return 1
    elif n<1 :
        return "enter valid non negative number"
    else:
        return n*factorial(n-1)
    

result = factorial(n)
print(result)
    